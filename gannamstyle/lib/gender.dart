import 'package:flutter/material.dart';

//Choose Gender
import 'package:smart_select/smart_select.dart';

//Next
import 'package:gannamstyle/feature.dart';

class ChooseGenderScreen extends StatefulWidget {
  final String imagePath;
  const ChooseGenderScreen({Key key, @required this.imagePath}) : super(key: key);

  @override
  _ChooseGenderScreenState createState() => _ChooseGenderScreenState();
}

class _ChooseGenderScreenState extends State<ChooseGenderScreen> {
  String value = 'man';
  List<S2Choice<String>> options = [
    S2Choice<String>(value: 'man', title: 'Man'),
    S2Choice<String>(value: 'woman', title: 'Woman')
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Choose Your Gender')),
      // 이미지는 디바이스에 파일로 저장됩니다. 이미지를 보여주기 위해 주어진
      // 경로로 `Image.file`을 생성하세요.
      body: Container(
        alignment: Alignment.center,
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            SmartSelect<String>.single(
                title: 'Gender',
                value: value,
                choiceItems: options,
                onChange: (state) => setState(() => value = state.value)
            ),
            //Text("Hello, ${myUser.myUser!.myProfileList[0].nickName}"),
            ElevatedButton(
                onPressed: () async {
                  Navigator.push(
                      context,
                      MaterialPageRoute(
                          builder: (context) => ChooseConvertImageScreen(
                            imagePath: widget.imagePath,
                            gender: value,
                          )));
                },
                child: Text('Next')),
          ],
        ),
      ),
    );
  }
}