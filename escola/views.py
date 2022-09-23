from rest_framework import viewsets
from .serializer import AlunoSerializer, CursoSerializer, MatriculaSerializer
from .models import Aluno, Curso, Matricula


class AlunosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os alunos(as)"""
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer


class CursosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os cursos"""
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class MatriculasViewSet(viewsets.ModelViewSet):
    """Exibindo todas as matrículas"""
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
