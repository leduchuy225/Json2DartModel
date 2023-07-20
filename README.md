# Dart Model Generator

Dart Modal Generator is a tool for automating the process of generating Dart model classes from JSON data. It takes JSON content as input and produces Dart classes that represent the structure of the JSON data.

## Prerequisites

- Python 3.x

## Usage

1. Paste json data on source.json
2. Run command `python3 generator {file_name}`

## Example 

1. source.json

```
{
   "name":"HT Logan",
   "age":23,
   "girl_friend":null,
   "friends":[
      "A",
      "B",
      "C"
   ],
   "watch_anime_days":[
      1,
      2,
      3,
      4
   ],
   "learn_flutter_days": []
}

```
1. Run `python3 generator about_me`

2. Result

```
import 'package:json_annotation/json_annotation.dart';

part 'about_me.g.dart';

@JsonSerializable()
class AboutMeModel {
@JsonKey(name: 'name')
final String? name;
@JsonKey(name: 'age')
final int? age;
@JsonKey(name: 'girl_friend')
final dynamic girlFriend; //Set type for this field
@JsonKey(name: 'friends')
final List<String>? friends;
@JsonKey(name: 'watch_anime_days')
final List<int>? watchAnimeDays;
@JsonKey(name: 'learn_flutter_days')
final List? learnFlutterDays; //Set type for this field

AboutMeModel({
this.name,
this.age,
this.girlFriend,
this.friends,
this.watchAnimeDays,
this.learnFlutterDays,
});

factory AboutMeModel.fromJson(Map<String, dynamic> json) => _$AboutMeModelFromJson(json);

Map<String, dynamic> toJson() => _$AboutMeModelToJson(this);
}
```