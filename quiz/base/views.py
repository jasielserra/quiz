from django.shortcuts import render, redirect
from quiz.base.models import Pergunta, Aluno
from quiz.forms import AlunoForm

# Create your views here.
def home(request):
    if request.method == 'POST':
        #Usuário já existe
        email = request.POST['email']
        try:
            aluno = Aluno.objects.get(email=email)
        except Aluno.DoesNotExist:
            # Usuário não existe
            formulario = AlunoForm(request.POST)
            if formulario.is_valid():
                aluno = formulario.save()
                request.session['aluno_id'] = aluno.id
                return redirect('/perguntas/1')
            else:
                contexto = {'formulario': formulario}
                return render(request, 'base/home.html', contexto)
        else:
            request.session['aluno_id'] = aluno.id
            return redirect('/perguntas/1')

    return render(request, 'base/home.html')

def perguntas(request, indice):
    try:
        aluno_id = request.session['aluno_id']
    except KeyError:
        return redirect('/')
    else:
        pergunta = Pergunta.objects.filter(disponivel=True).order_by('id')[indice-1]
        contexto = {'indice_da_questao': indice, 'pergunta': pergunta}
        if request.method == 'POST':
            resposta_indice = int(request.POST['resposta_indice'])
            if resposta_indice == pergunta.alternativa_correta:
                # Armazenar dados da resposta
                return redirect(f'/perguntas/{indice + 1}')
            contexto['resposta_indice'] = resposta_indice
        return render(request, 'base/game.html', context=contexto)

def classificacao(request):
    return render(request, 'base/classificacao.html')