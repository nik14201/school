from parent.models import Parent,    TokenParent
from teacher.models import Teacher,  TokenTeacher
from student.models import Student,  TokenStudent
from profiles.models import Profile, TokenProfile

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


