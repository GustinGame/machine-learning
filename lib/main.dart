import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: ChatScreen(),
    );
  }
}

class ChatScreen extends StatefulWidget {
  @override
  _ChatScreenState createState() => _ChatScreenState();
}

class _ChatScreenState extends State<ChatScreen> {
  TextEditingController _messageController = TextEditingController();
  List<ChatMessage> _chatMessages = [];

  _sendMessage(String message) async {
    // Call to the ChatGPT API
    final response = await http.post(
      Uri.parse(
          'http://127.0.0.1:5000/predict'), // Replace with the actual API URL
      body: {'message': message},
    );

    if (response.statusCode == 200) {
      setState(() {
        _chatMessages.add(ChatMessage(
          text: message,
          isUser: true, // Indicate that the message is from the user
        ));
        _chatMessages.add(ChatMessage(
          text: response.body,
          isUser: false, // Indicate that the message is from the ChatGPT API
        ));
      });

      // Show a SnackBar after sending the message
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(
          content: Text('Message sent: $message'),
          duration: Duration(seconds: 2),
        ),
      );
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('ChatGPT App'),
      ),
      body: Column(
        children: [
          Expanded(
            child: ListView.builder(
              itemCount: _chatMessages.length,
              itemBuilder: (context, index) {
                return _chatMessages[index];
              },
            ),
          ),
          Padding(
            padding: const EdgeInsets.all(8.0),
            child: Row(
              children: [
                Expanded(
                  child: TextField(
                    controller: _messageController,
                    decoration: InputDecoration(
                      hintText: 'Type your message...',
                    ),
                  ),
                ),
                IconButton(
                  icon: Icon(Icons.send),
                  onPressed: () {
                    String message = _messageController.text;
                    if (message.isNotEmpty) {
                      _sendMessage(message);
                      _messageController.clear();
                    }
                  },
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}

class ChatMessage extends StatelessWidget {
  final String text;
  final bool isUser;

  ChatMessage({required this.text, required this.isUser});

  @override
  Widget build(BuildContext context) {
    return Container(
      margin: EdgeInsets.symmetric(vertical: 10),
      alignment: isUser ? Alignment.centerRight : Alignment.centerLeft,
      child: Container(
        padding: EdgeInsets.all(10),
        decoration: BoxDecoration(
          color: isUser ? Colors.blue : Colors.grey,
          borderRadius: BorderRadius.circular(8),
        ),
        child: Text(
          text,
          style: TextStyle(color: Colors.white),
        ),
      ),
    );
  }
}
