@echo off
cd server 
start cmd /k python app.py

timeout /t 5

cd ..  
flutter run -d chrome