from parent.models import User as Parent,  Token as TokenParent
from teacher.models import User as Teacher, Token as TokenTeacher
from student.models import User as Student, Token as TokenStudent
from profiles.models import User as Profile, Token as TokenProfile

from parent.serializers import TokenSerializer as TokenParentSerializer
from teacher.serializers import TokenSerializer as TokenTeacherSerializer
from student.serializers import TokenSerializer as TokenStudentSerializer
from profiles.serializers import TokenSerializer as TokenProfileSerializer

def get_token_model(user):
    if isinstance(user, Parent):
        return TokenParent
    elif isinstance(user, Teacher):
        return TokenTeacher
    elif isinstance(user, Student):
        return TokenStudent
    elif isinstance(user, Profile):
        return TokenProfile

def get_token_serializers(user):
    if isinstance(user, Parent):
        return TokenParentSerializer
    elif isinstance(user, Teacher):
        return TokenTeacherSerializer
    elif isinstance(user, Student):
        return TokenStudentSerializer
    elif isinstance(user, Profile):
        return TokenProfileSerializer


def get_token_model_auth(User):
    user=User()
    if isinstance(user, Teacher):
        del user
        return TokenTeacher
    elif isinstance(user, Student):
        del user
        return TokenStudent
    elif isinstance(user, Profile):
        del user
        return TokenProfile
    elif isinstance(user, Parent):
        del user
        return TokenParent
    else:
        del user
        return None