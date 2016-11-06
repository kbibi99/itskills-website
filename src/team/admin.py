from django.contrib import admin
from .models import (TeamTitle,Education, InternShip, Profile, Projects,Skill_title,
                     Skills, SocialExperience, WorkExperience, Recongnitions,
                     Interests, Email, PhoneNumber, SotialNetAdress)
# Register your models here.


class TeamTitleModelAdmin(admin.ModelAdmin):
    list_display = ["user"]

    class Meta:
        model = TeamTitle


admin.site.register(TeamTitle, TeamTitleModelAdmin)

class EducationModelAdmin(admin.ModelAdmin):
    list_display = ["owner"]

    class Meta:
        model = Education


admin.site.register(Education, EducationModelAdmin)


class InternShipModelAdmin(admin.ModelAdmin):
    list_display = ["owner"]

    class Meta:
        model = InternShip


admin.site.register(InternShip, InternShipModelAdmin)

class ProfileModelAdmin(admin.ModelAdmin):
    list_display = ["slug","first_name", "last_name"]

    class Meta:
        model = Profile


admin.site.register(Profile, ProfileModelAdmin)

class EmailModelAdmin(admin.ModelAdmin):
    list_display = ["owner", "e_mail"]

    class Meta:
        model = Email


admin.site.register(Email, EmailModelAdmin)

class PhoneNumberModelAdmin(admin.ModelAdmin):
    list_display = ["owner", "phone_number"]

    class Meta:
        model = PhoneNumber


admin.site.register(PhoneNumber, PhoneNumberModelAdmin)


class SotialNetAdressModelAdmin(admin.ModelAdmin):
    list_display = ["owner", "sotial_network_adress"]

    class Meta:
        model = SotialNetAdress


admin.site.register(SotialNetAdress, SotialNetAdressModelAdmin)

class ProjectsModelAdmin(admin.ModelAdmin):
    list_display = ["owner"]

    class Meta:
        model = Projects


admin.site.register(Projects, ProjectsModelAdmin)




class SkillsTitleModelAdmin(admin.ModelAdmin):
    list_display = ["owner"]

    class Meta:
        model = Skill_title


admin.site.register(Skill_title, SkillsTitleModelAdmin)


class SkillsModelAdmin(admin.ModelAdmin):
    list_display = ["skill_title"]

    class Meta:
        model = Skills

admin.site.register(Skills, SkillsModelAdmin)


class SocialExperienceModelAdmin(admin.ModelAdmin):
    list_display = ["owner"]

    class Meta:
        model = SocialExperience


admin.site.register(SocialExperience, SocialExperienceModelAdmin)


class WorkExperienceModelAdmin(admin.ModelAdmin):
    list_display = ["owner"]

    class Meta:
        model = WorkExperience


admin.site.register(WorkExperience, WorkExperienceModelAdmin)


class RecongnitionsModelAdmin(admin.ModelAdmin):
    list_display = ["owner"]

    class Meta:
        model = Recongnitions


admin.site.register(Recongnitions, RecongnitionsModelAdmin)



class InterestsModelAdmin(admin.ModelAdmin):
    list_display = ["owner"]

    class Meta:
        model = Interests


admin.site.register(Interests, InterestsModelAdmin)