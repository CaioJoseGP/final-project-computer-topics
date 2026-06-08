# 🚀 Como Executar a Aplicação com Kubernetes

Este é um guia rápido e prático para colocar a aplicação para funcionar utilizando **Docker** e **Kubernetes**. Siga os passos abaixo para configurar o ambiente e inicializar todos os recursos.

---

## 🛠️ Passo 1: Inicializar o Docker & Kubernetes

Antes de rodar os comandos, certifique-se de que o seu cluster local está ativo:

1. **Abra o Docker Desktop** (ou a ferramenta de sua preferência) e certifique-se de que o serviço do Docker está rodando.
2. **Ative o Kubernetes** nas configurações do seu Docker Desktop.
3. 💡 *Recomendação:* É altamente recomendável estar logado no **Docker Hub** para evitar problemas com limites de download (*rate limiting*) de imagens públicas ou privadas.

---

## 💻 Passo 2: Implantar os Recursos no Kubernetes

Com o cluster pronto, abra o terminal na raiz do projeto (onde a pasta `./k8s` está localizada) e execute o seguinte comando:

```bash
kubectl apply -f ./k8s
```

### 🔍 O que esse comando faz nos bastidores?
* **Ativação do HPA (Horizontal Pod Autoscaler):** Configura o escalonamento automático dos Pods com base no uso de recursos.
* **System Monitor ("Os Olhos"):** Inicializa as ferramentas de monitoramento para dar visibilidade total sobre a saúde e a performance do cluster.
* **Simulação com Hanoi:** Iniciará um processo de carga (Hanoi) que aumentará o consumo de recursos automaticamente para testar o comportamento do HPA na prática.

---

## 📊 Passo 3: Monitoramento e Acesso

Agora que tudo está rodando, você pode interagir com o ambiente através dos seguintes endereços e comandos:

### 🌐 Portas Locais
* **Aplicação:** Acesse [http://localhost:5000](http://localhost:5000) para interagir com a interface ou API da aplicação.
* **Banco de Dados (MySQL):** Conecte seu client favorito (DBeaver, MySQL Workbench, etc.) em `localhost:3306`.

### 📜 Acompanhando os Logs do HPA
Para ver o Kubernetes reagindo ao aumento de consumo provocado pelo Hanoi e criando novos Pods automaticamente, execute no terminal:

```bash
kubectl get hpa -w
```

---
✨ *Pronto! Sua aplicação está rodando e sendo monitorada automaticamente pelo Kubernetes.*
