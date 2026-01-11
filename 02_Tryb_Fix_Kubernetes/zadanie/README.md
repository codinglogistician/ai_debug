
# Ćwiczenia z Gradio na kubernetescie

### Zadanie 1. Uruchom Gradio lokalnie

1. Stwórz plik `app.py` z kodem (Prosty interace bez modelu). 
2. Zainstaluj Gradio. 
3. Uruchom aplikację.
4. Otwórz link w terminalu i sprawdź działanie aplikacji.

---

### Zadanie 2. Zapakuj aplikację w Dockera

1. Stwórz plik `Dockerfile`.
2. Zbuduj obraz Dockera:

3. Uruchom kontener.

---

### Zadanie 3. Uruchom Gradio w Kubernetesie

1. Stwórz plik `gradio-pod.yaml`.
2. Stwórz plik `gradio-service.yaml`.
3. Uruchom w Kubernetesie. 
4. Otwórz aplikację w przeglądarce:

   ```bash
   minikube service gradio-service
   ```

---
