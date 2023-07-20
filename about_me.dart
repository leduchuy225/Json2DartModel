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
