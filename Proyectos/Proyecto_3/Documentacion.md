# Proyecto 3: Ética Médica y Bioética en la Era de la IA

**Alumno:**  
- Melvin Marin Gonzalez (21120229)  

---

## 1. Introducción

Este proyecto documenta la construcción de un corpus y el uso de un modelo de lenguaje natural (con técnicas de embeddings y fine-tuning) para analizar preguntas clave en torno a la autonomía personal, el inicio de la vida y la eutanasia. Partimos de archivos PDF revisados (publicaciones académicas, guías éticas, legislación) y búsquedas en Google Académico para crear un dataset especializado. Luego entrenamos un modelo (por ejemplo, mediante Ollama) para generar respuestas rigurosas sobre dilemas bioéticos complejos.

> **Nota:**  
> - La IA ha sido instruida para responder como un profesional especializado en ética médica y bioética, garantizando que las respuestas sean rigurosas, fundamentadas y equilibradas, con citas de teorías reconocidas.  
> - Este enfoque académico evita sesgos personales y sintetiza información desde fuentes confiables, sin emitir opiniones propias.

---

## 2. Dataset y Recolección de Información

1. **Fuentes Primarias (PDFs Subidos)**
   - Artículos académicos sobre ética del aborto y eutanasia.
   - Normativas y resoluciones legales (p. ej., sentencias de tribunales, leyes nacionales).
   - Ensayos y capítulos de libros en derecho, bioética y filosofía moral (Kant, Mill, Nussbaum, etc.).

2. **Búsquedas en Google Académico**
   - Términos clave:  
     - “autonomía bioética”  
     - “derecho al aborto”  
     - “eutanasia y dignidad humana”  
     - “IA en decisiones médicas”  
     - “ética del cuidado y aborto”  
     - “deontología aborto”  
     - “utilitarismo y eutanasia”  
   - Se seleccionaron trabajos muy citados y recientes (últimos 5 años).
   - Extracción de fragmentos relevantes para enriquecer el modelo.

3. **Procesamiento y Pre-entrenamiento**
   - Conversión de PDFs a texto, limpieza y normalización.
   - Extracción de párrafos con definiciones teóricas y casos legales concretos.

---

## 3. Preguntas Analizadas y Explicación de Respuestas

A cada pregunta, la IA generó un texto que incluye argumentos y perspectivas desde distintas corrientes éticas, filosóficas y legales. En esta sección se resume brevemente cada respuesta.

### 3.1. ¿Tiene una persona el derecho exclusivo a decidir sobre su cuerpo cuando hay otra vida en desarrollo?

- **Resumen de la Respuesta IA:**  
 La autonomía personal es un principio central en bioética, pero también se reconocen los derechos inherentes de la vida en desarrollo. Se destacan visiones desde los derechos humanos, la ética kantiana y teorías deontológicas y utilitaristas. La IA sugiere que no existe un derecho absoluto, sino un equilibrio entre el derecho a decidir y la protección de la vida.

---


### 3.2. ¿Hasta qué punto el lenguaje utilizado (“interrupción” vs. “terminación”) influye en la percepción ética del aborto?

- **Resumen de la Respuesta IA:**  
 El lenguaje afecta emocional y éticamente la percepción del aborto. "Interrupción" puede evocar violencia o trauma, mientras que "terminación" sugiere un acto más neutral y consciente. La IA resalta la importancia de un lenguaje respetuoso y libre de estigmas para facilitar un diálogo más empático y objetivo.
---

### 3.3. ¿Qué principios éticos (utilitarismo, deontología, ética del cuidado) pueden respaldar o rechazar el aborto inducido?

- **Resumen de la Respuesta IA:**  
  El utilitarismo, la deontología y la ética del cuidado ofrecen argumentos tanto a favor como en contra del aborto inducido. También se consideran principios como no maleficencia, beneficencia y autonomía. La IA destaca la diversidad de enfoques y la necesidad de considerar múltiples perspectivas al abordar este dilema.

---

### 3.4. ¿Puede una inteligencia artificial participar de forma ética en decisiones sobre aborto?

- **Resumen de la Respuesta IA:**  
La IA puede aportar análisis objetivos y procesamiento de información médica, pero enfrenta limitaciones como la falta de comprensión emocional, sesgos algorítmicos y cuestiones de responsabilidad moral. Se enfatiza su uso como herramienta complementaria bajo supervisión humana y regulaciones claras.
---

### 3.5. ¿Qué riesgos éticos implica delegar información médica sensible a sistemas automatizados?

- **Resumen de la Respuesta IA:**  
Existen riesgos relacionados con la privacidad, los sesgos, la comprensión emocional, la responsabilidad y la relación médico-paciente. La IA propone medidas de mitigación como transparencia, seguridad de datos y formación ética continua para los profesionales de la salud.

  1. **Privacidad y confidencialidad:** Fallos de seguridad pueden exponer datos personales.  
  2. **Breach de confianza:** Profesionales pueden desconfiar de la tecnología; pacientes, de su manejo.  
  3. **Sesgos en tratamiento:** Algoritmos replican desigualdades (género, etnia, clase).  
  4. **Falta de comprensión humana:** Máquinas no captan contexto emocional.  
  5. **Dependencia tecnológica:** Riesgo de perder habilidades clínicas esenciales.  
  6. **Errores y responsabilidad difusa:** ¿Quién asume culpa si el sistema falla?  
  7. **Impacto en relación médico-paciente:** IA no puede reemplazar empatía y contacto humano.  
  8. **Influencia en decisiones clínicas:** IA puede condicionar juicios sin pleno consentimiento.  

---

### 3.6. ¿Es éticamente válido que una persona decida poner fin a su vida en situaciones de sufrimiento irreversible?

- **Resumen de la Respuesta IA:**  
Se presentan argumentos centrados en la autonomía y dignidad personal, así como objeciones basadas en el valor intrínseco de la vida y la posibilidad de alternativas paliativas. La IA destaca la complejidad del tema y la necesidad de procedimientos rigurosos y evaluación cuidadosa.

---

### 3.7. ¿Cuál es la diferencia entre eutanasia activa, pasiva y el suicidio asistido? ¿Importa éticamente?

- **Resumen de la Respuesta IA:**  
 Se diferencian según el grado de intervención directa. La eutanasia activa implica una acción directa para causar la muerte, la pasiva consiste en suspender tratamientos y el suicidio asistido en proveer medios para que el paciente decida. Cada forma tiene implicaciones éticas distintas que deben evaluarse según el contexto.
---

### 3.8. ¿Qué papel podrían (o no deberían) tener los sistemas de inteligencia artificial en este tipo de decisiones?

- **Resumen de la Respuesta IA:**  
 La IA puede apoyar con análisis de datos y evaluación médica, pero se deben considerar los riesgos como la pérdida de autonomía clínica, la falta de empatía y los sesgos. Se subraya la necesidad de regulación, transparencia y supervisión ética constante.

---

### 3.9. ¿Qué sucede cuando el deseo de morir entra en conflicto con creencias religiosas, leyes o protocolos médicos?

- **Resumen de la Respuesta IA:**  
 Surgen dilemas complejos que requieren mediación y diálogo. Se proponen estrategias como el acompañamiento espiritual, la revisión legal, la actualización de protocolos médicos y la educación continua. Se enfatiza la importancia del respeto y la comunicación interdisciplinaria.
  Reconoce la **autonomía individual**, pero afirma que las normas religiosas, legales y médicas son fuerzas normativas que requieren mediación.  

---

### 3.10. ¿Se puede hablar de una “muerte digna” sin considerar el contexto emocional y humano?

- **Resumen de la Respuesta IA:**  
La IA sostiene que una muerte digna no puede definirse solo desde lo médico. Es esencial incluir dimensiones emocionales, culturales y éticas, así como ofrecer apoyo emocional y comunicación abierta entre paciente, familia y equipo médico.

---

# 4. Conclusión General

La experiencia con esta IA demuestra que, para abordar dilemas éticos complejos sobre autonomía y fin de vida, el modelo requiere un entrenamiento profundo y contextualizado. En particular:

- **Importancia del Contexto para el Entrenamiento**  
  Los datos de entrenamiento deben incluir fundamentos filosóficos, sentencias legales y guías clínicas actualizadas. Esto garantiza que la IA incorpore matices históricos, jurídicos y culturales esenciales para el análisis.

- **Equilibrio en la Respuesta**  
  Sin un marco ético y legal adecuado, la IA carecería de la capacidad para presentar argumentos balanceados. El contexto proporciona los criterios necesarios para evaluar las múltiples perspectivas.

- **Rol de Apoyo a la Investigación**  
  Una IA bien entrenada actúa como asistente de investigación, sintetizando información académica y permitiendo agilizar la revisión de literatura y jurisprudencia.

En resumen, entrenar esta IA exige proporcionar un contexto amplio y diverso que cubra teorías éticas, sentencias relevantes y protocolos médicos. Solo así podremos confiar en que las respuestas apoyan de forma rigurosa cualquier investigación sobre ética médica y bioética.

Este proyecto demuestra que, para que una IA responda como experta en ética médica y bioética, es imprescindible entrenarla con un contexto amplio y diversificado:

## Fundamentos Filosóficos y Éticos

- Incluir textos de Kant, Mill, Rawls, Nussbaum, entre otros, para abarcar utilitarismo, deontología y ética del cuidado.
- De esta manera, la IA comprende la pluralidad de argumentos y matices necesarios para el debate sobre autonomía, aborto y fin de vida.

## Marco Legal y Jurisprudencial

- Incorporar sentencias fundamentales (FAL en Argentina, Roe v. Wade / Dobbs v. Jackson en EE. UU.) y normas nacionales/internacionales (Declaración Universal sobre Bioética, directrices de la OMS).
- Así, la IA sitúa cada dilema en el contexto normativo vigente y valora sus implicaciones legales.

## Protocolos Clínicos y Guías Médicas

- Añadir manuales de cuidados paliativos y medicina terminal, junto con protocolos de confidencialidad y manejo de datos médicos.
- El modelo conoce los estándares clínicos y los riesgos éticos de delegar información a sistemas automatizados.

## Resultados y Enseñanzas

Cada pregunta se abordó con un análisis equilibrado: autonomía versus protección de la vida en desarrollo, impacto del lenguaje, principios éticos contrapuestos, ventajas y riesgos de la IA, diferencias entre eutanasia activa/pasiva, conflicto entre deseo de morir y creencias, y la importancia del contexto emocional para definir una “muerte digna”.

### Aprendizajes clave

- **Pluralidad de Perspectivas**  
  No existe un único veredicto ético; cada corriente filosófica aporta razones válidas.

- **IA como Herramienta Complementaria**  
  Debe apoyar el análisis de evidencia, pero no reemplazar el juicio humano interdisciplinario.

- **Lenguaje y Estigmas**  
  Términos neutros (“terminación”) reducen prejuicios y facilitan discusiones respetuosas.

- **Dimensión Humana**  
  El componente emocional y cultural es indispensable en cualquier debate sobre aborto o fin de vida.

## Siguientes Pasos para el Entrenamiento

### Dataset Enriquecido

- Simulaciones de casos clínicos reales para afinar al modelo en escenarios prácticos.  
- Incorporar literatura emergente y jurisprudencia reciente para mantener la base de conocimientos actualizada.

### Módulo de Explainable AI

- Desarrollar mecanismos que muestren el razonamiento detrás de cada recomendación.

### Validación Continua

- Encuestar a profesionales de la salud y bioética para medir la precisión y utilidad de las respuestas.  
- Adaptar el modelo según retroalimentación de médicos, filósofos y juristas.


# 5. Anexos

- **Video del proyecto**  
  [Ver video explicativo](https://itecm-my.sharepoint.com/:v:/g/personal/l21120229_morelia_tecnm_mx/EXwdgrvCsClFrQ0aX5le808BL580Ty2GFaCQXhLs79CHWw)  
  *(Video alojado en SharePoint con una demostración y explicación del desarrollo del proyecto, su metodología y resultados principales.)*

  [.rar de los pdfs](https://itecm-my.sharepoint.com/:u:/g/personal/l21120229_morelia_tecnm_mx/EfxUS4iK98NJjuCrlXXUfD4Bl2_W6cathVyJ36gFpCyaaA?e=v0wfGg) 
  *(Contiene todos los archivos PDF que se utilizaron para entrenar la IA.)*