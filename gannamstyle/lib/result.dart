import 'package:flutter/material.dart';
import 'dart:io';

//for Demo Version
import 'package:gannamstyle/main.dart';

class ResultScreen extends StatelessWidget {
  final String imagePath;

  const ResultScreen({Key key, this.imagePath}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Result')),
      // 이미지는 디바이스에 파일로 저장됩니다. 이미지를 보여주기 위해 주어진
      // 경로로 `Image.file`을 생성하세요.
      body: Image.file(File(imagePath)),
      floatingActionButton: FloatingActionButton.extended(
        onPressed: () {
          Navigator.push(
              context,
              MaterialPageRoute(
                  builder: (context) => MainPage()));
        },
        label: Text('Save'),
      ),
    );
  }
}