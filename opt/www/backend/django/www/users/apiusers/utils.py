from parentuser.models import ParentUser, TokenParent
from teacher.models import Teacher,  TokenTeacher
from student.models import Student,  TokenStudent
from profileuser.models import ProfileUser, TokenProfile

from parentuser.serializers import TokenSerializer as TokenParentSerializer
from teacher.serializers import TokenSerializer as TokenTeacherSerializer
from student.serializers import TokenSerializer as TokenStudentSerializer
from profileuser.serializers import TokenSerializer as TokenProfileSerializer

def get_token_model(user):
    if isinstance(user, ParentUser):
        return TokenParent
    elif isinstance(user, Teacher):
        return TokenTeacher
    elif isinstance(user, Student):
        return TokenStudent
    elif isinstance(user, ProfileUser):
        return TokenProfile

def get_token_serializers(user):
    if isinstance(user, ParentUser):
        return TokenParentSerializer
    elif isinstance(user, Teacher):
        return TokenTeacherSerializer
    elif isinstance(user, Student):
        return TokenStudentSerializer
    elif isinstance(user, ProfileUser):
        return TokenProfileSerializer


