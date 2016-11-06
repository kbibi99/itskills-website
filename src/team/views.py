try:
    from urllib import quote_plus #python 2
except:
    pass

try:
    from urllib.parse import quote_plus #python 3
except: 
    pass
from django.db.models import Q
from django.shortcuts import get_object_or_404, render

from .models import (Education, Email, Interests, InternShip, PhoneNumber,
                     Profile, Projects, Recongnitions, Skill_title, Skills,
                     SocialExperience, SotialNetAdress, WorkExperience)


# Create your views here.



def team_detail(request, slug=None):
    instance = get_object_or_404(Profile, slug=slug)
    
    # email_instance=Email.objects.get(pk=instance.id)
    email_instance=list(Email.objects.filter(owner=instance.id))
    phone_numberinstance=list(PhoneNumber.objects.filter(owner=instance.id))
    education_instance =list(Education.objects.filter(owner=instance.id))
    internship_instance =list(InternShip.objects.filter(owner=instance.id))
    projects_instance =list(Projects.objects.filter(owner=instance.id))
    # skills_title_instance= get_object_or_404(Skill_title, owner=instance.id)
    skills_title_instance =list(Skill_title.objects.filter(owner=instance.id))
    # skills_instance =list(Skills.objects.filter(skill_title=skills_title_instance.skill_title_id))
    skills_instance =Skills.objects.all()
    # skills_instance =list(Skills.objects.filter(skill_title=skills_title_instance.0.skill_title))
    social_exp_instance =list(SocialExperience.objects.filter(owner=instance.id))
    work_exp_instance =list(WorkExperience.objects.filter(owner=instance.id))
    recognitions_instance=list(Recongnitions.objects.filter(owner=instance.id))
    interests_instance=list(Interests.objects.filter(owner=instance.id))


    context = {
        "profile": instance,
        "email":email_instance,
        "phone_number":phone_numberinstance,
        "education":education_instance,
        "internship":internship_instance,
        "projects":projects_instance,
        "skills_title":skills_title_instance,
        "skills":skills_instance,
        "social_experience":social_exp_instance,
        "work_exp":work_exp_instance,
        "recognitions":recognitions_instance,
        "interests":interests_instance,
    }
    return render(request, "team/details.html", context)


# def SkillInstance(SkillTitleIndex):
#     skills_instance =list(Skills.objects.filter(skill_title=skills_title_instance.SkillTitleIndex.skill_title)
#     return skills_instance


def cut(value, arg):
    """Removes all values of arg from the given string"""
    return value.replace(arg, ' ')