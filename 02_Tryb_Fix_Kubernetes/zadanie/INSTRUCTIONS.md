# Przewodnik Wdrażania Aplikacji Gradio

Ten katalog zawiera wszystkie pliki potrzebne do wdrożenia prostej aplikacji Gradio do przetwarzania tekstu lokalnie, w Dockerze i na Kubernetesie.

## Przegląd Plików

- **app.py**: Prosta aplikacja Gradio, która odwraca tekst i dostarcza statystyk
- **requirements.txt**: Zależności Pythona (Gradio)
- **Dockerfile**: Definicja obrazu kontenera
- **gradio-pod.yaml**: Manifest Poda Kubernetes
- **gradio-service.yaml**: Manifest Serwisu Kubernetes (NodePort)

## Zadanie 1: Uruchom Gradio Lokalnie

1. **Zainstaluj zależności:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Uruchom aplikację:**
   ```bash
   python app.py
   ```

3. **Otwórz aplikację:**
   - Otwórz URL pokazany w terminalu (zazwyczaj http://127.0.0.1:7860)
   - Wpisz jakiś tekst, aby zobaczyć go odwróconego wraz ze statystykami

## Zadanie 2: Uruchom w Dockerze

1. **Zbuduj obraz Dockera:**
   ```bash
   docker build -t gradio-app:latest .
   ```

2. **Uruchom kontener:**
   ```bash
   docker run -p 7860:7860 gradio-app:latest
   ```

3. **Otwórz aplikację:**
   - Otwórz http://localhost:7860 w przeglądarce

## Zadanie 3: Uruchom w Kubernetesie (Minikube)

### Wymagania
- Minikube zainstalowany i uruchomiony (`minikube start`)
- kubectl skonfigurowany do użycia kontekstu Minikube

### Kroki Wdrożenia

1. **Skonfiguruj Dockera do użycia demona Docker z Minikube:**
   ```bash
   eval $(minikube docker-env)
   ```

2. **Zbuduj obraz Dockera w Minikube:**
   ```bash
   docker build -t gradio-app:latest .
   ```

3. **Wdróż Poda:**
   ```bash
   kubectl apply -f gradio-pod.yaml
   ```

4. **Wdróż Serwis:**
   ```bash
   kubectl apply -f gradio-service.yaml
   ```

5. **Zweryfikuj wdrożenie:**
   ```bash
   kubectl get pods
   kubectl get services
   ```

6. **Otwórz aplikację:**
   ```bash
   minikube service gradio-service
   ```
   Ta komenda automatycznie otworzy aplikację w domyślnej przeglądarce.

### Rozwiązywanie Problemów

- **Sprawdź status poda:**
  ```bash
  kubectl describe pod gradio-pod
  kubectl logs gradio-pod
  ```

- **Sprawdź serwis:**
  ```bash
  kubectl describe service gradio-service
  ```

- **Ręczny dostęp do URL:**
  ```bash
  minikube service gradio-service --url
  ```

### Czyszczenie

Aby usunąć zasoby Kubernetes:
```bash
kubectl delete -f gradio-service.yaml
kubectl delete -f gradio-pod.yaml
```

## Architektura

```
Przeglądarka → Serwis NodePort → Pod → Kontener Docker → Aplikacja Gradio (port 7860)
```

## Uwagi

- Aplikacja łączy się z `0.0.0.0:7860`, aby umożliwić dostęp z zewnątrz z Dockera/Kubernetesa
- Pod używa `imagePullPolicy: Never`, aby użyć lokalnie zbudowanego obrazu
- Serwis używa typu `NodePort` dla dostępu zewnętrznego przez Minikube
- Etykiety `app: gradio` i `tier: frontend` łączą Serwis z Podem
