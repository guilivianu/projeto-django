import random
from django.core.management.base import BaseCommand
from django.utils import timezone
from core.models import User, Problema, Especialidade, PerfilOficina

class Command(BaseCommand):
    help = 'Popula o banco de dados com usuários, oficinas e problemas aleatórios'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.WARNING('Iniciando o processo de população do banco...'))

        # 1. Listas de Dados para Sorteio
        nomes_clientes = ['Ana', 'Bruno', 'Carlos', 'Daniela', 'Eduardo', 'Fernanda', 'Gabriel', 'Helena']
        sobrenomes = ['Silva', 'Santos', 'Oliveira', 'Souza', 'Pereira', 'Lima']
        
        carros = ['Fiat Uno', 'VW Gol', 'Honda Civic', 'Toyota Corolla', 'Ford Ka', 'Chevrolet Onix', 'Jeep Renegade']
        
        lista_problemas = [
            ('Motor fazendo barulho', 'O motor apresenta um ruído metálico ao acelerar acima de 3000 giros.'),
            ('Freio assobiando', 'Toda vez que piso no freio faz um barulho agudo, parece pastilha gasta.'),
            ('Ar condicionado não gela', 'Sai apenas vento quente, mesmo na temperatura mínima.'),
            ('Luz da injeção acesa', 'A luz acendeu no painel ontem e o carro perdeu potência na subida.'),
            ('Volante tremendo', 'Ao passar de 80km/h o volante começa a vibrar muito.'),
            ('Vazamento de óleo', 'Encontrei uma poça de óleo na garagem hoje de manhã.'),
            ('Marcha arranhando', 'A segunda marcha está difícil de entrar e faz barulho.'),
        ]

        lista_especialidades = ['Suspensão', 'Motor', 'Elétrica', 'Freios', 'Injeção Eletrônica', 'Câmbio', 'Funilaria']

        # 2. Criar Especialidades
        self.stdout.write('Criando especialidades...')
        objs_especialidades = []
        for nome in lista_especialidades:
            esp, created = Especialidade.objects.get_or_create(nome=nome)
            objs_especialidades.append(esp)

        # 3. Criar Oficinas (Mecânicos)
        self.stdout.write('Criando oficinas...')
        for i in range(1, 4): # Cria 3 oficinas
            username = f'oficina{i}'
            if not User.objects.filter(username=username).exists():
                user = User.objects.create_user(username=username, email=f'{username}@email.com', password='123')
                user.is_oficina = True
                user.save()
                
                # Cria o Perfil
                perfil = PerfilOficina.objects.create(
                    usuario=user,
                    nome_oficina=f'Auto Center {username.title()}',
                    endereco=f'Rua das Oficinas, {i * 100}'
                )
                # Adiciona 3 especialidades aleatórias
                perfil.especialidades.set(random.sample(objs_especialidades, 3))
                perfil.save()

        # 4. Criar Clientes e Distribuir Problemas
        self.stdout.write('Criando clientes e gerando problemas aleatórios...')
        
        for nome in nomes_clientes:
            # Gera um username único combinando nome e número aleatório
            username = f"{nome.lower()}{random.randint(1, 99)}"
            
            if not User.objects.filter(username=username).exists():
                # Cria o usuário Cliente
                user = User.objects.create_user(username=username, email=f'{username}@email.com', password='123')
                user.is_cliente = True
                user.first_name = nome
                user.last_name = random.choice(sobrenomes)
                user.save()

                # Sorteia quantos problemas esse cliente terá (entre 1 e 3)
                qtd_problemas = random.randint(1, 3)

                for _ in range(qtd_problemas):
                    # Escolhe um carro e um problema aleatório
                    carro_escolhido = random.choice(carros)
                    titulo_prob, desc_prob = random.choice(lista_problemas)

                    Problema.objects.create(
                        cliente=user,
                        titulo=titulo_prob,
                        modelo_carro=carro_escolhido,
                        descricao=f"{desc_prob} (Ocorrido no {carro_escolhido})",
                        status='ABERTO'
                    )

        self.stdout.write(self.style.SUCCESS('Concluído! Banco de dados populado com sucesso.'))