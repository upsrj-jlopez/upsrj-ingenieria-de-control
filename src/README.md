# Práctica: Diseño de realimentación para cumplir requisitos de respuesta térmica en un invernadero  
## Contexto industrial  
Estás diseñando un sistema de control de temperatura para un invernadero pequeño (50 cm – 1 m de lado) construido en acrílico. El sistema debe cumplir con un requisito de tiempo de establecimiento para garantizar que la temperatura interna alcance rápidamente el valor deseado, evitando fluctuaciones que afecten el crecimiento de las plantas.  

La fuente de calor puede ser una resistencia eléctrica o lámpara de calefacción, y el invernadero presenta pérdidas de calor por conducción a través del acrílico y por ventilación.  

## Objetivo  
Determinar los parámetros térmicos del invernadero ($\tau$ y $\alpha$) para que el sistema cumpla con un tiempo de establecimiento especificado, considerando las características físicas del prototipo construido por cada alumno.  

## Fundamento teórico  
La función de transferencia del invernadero con pérdidas adicionales se modela como:  

$$
F(s) = \frac{1}{\tau s + 1 + \alpha}
$$

- $\tau$: constante de tiempo térmica, relacionada con la masa de aire y el coeficiente de pérdidas.  
- $\alpha$: factor adimensional que representa pérdidas adicionales (ventilación, fugas).  

El polo del sistema está en:  

$$
p = -\frac{1 + \alpha}{\tau}
$$

Y el tiempo de establecimiento aproximado es:  

$$
t_s \approx \frac{4}{|p|}
$$

## Actividad  
1. Calcula la **constante de tiempo térmica $\tau$** de tu invernadero:  
   - Determina el volumen $V$ del invernadero.  
   - Calcula la masa de aire: $m = \rho \cdot V$, con $\rho \approx 1.2 \, kg/m^3$.  
   - Obtén la capacidad térmica: $C_{th} = m \cdot c_p$, con $c_p \approx 1000 \, J/(kg \cdot K)$.  
   - Estima el área de paredes y techo $A$.  
   - Usa un coeficiente de transferencia de calor $h$ (5–10 W/(m²·K) para acrílico).  
   - Calcula: $\tau = \frac{C_{th}}{hA}$.  

2. Propón un valor de **$\alpha$** según el nivel de ventilación o fugas de tu diseño:  
   - Invernadero bien sellado: $\alpha \approx 0.1$.  
   - Ventilación ligera: $\alpha \approx 0.3$.  
   - Ventilación fuerte: $\alpha \approx 0.5$.  

3. Calcula el polo dominante para tu sistema:  
   $$
   p = -\frac{1 + \alpha}{\tau}
   $$

4. Estima el polo para los tiempos de establecimiento deseados: $t_s = 300s, 600s, 900s, 1200s, 1500s$.  
   Usa la relación:  
   $$
   t_s \approx \frac{4}{|p|}
   $$

5. Implementa la función de transferencia en `greenhouse_temp(tau, alpha)` dentro de `control_system/plant.py`:  

6. Simula la respuesta al escalón con los distintos tiempos de establecimiento $t_s = 300s, 600s, 900s, 1200s, 1500s$.  
   - Genera una gráfica por cada caso.  
   - Las tres gráficas deben estar en `build/out`.  

7. Registra los resultados en `build/out/register.csv` mediante `add_entry(tau, alpha, ts, pole)`.  

8. Valida que el sistema cumple con el requisito observando las gráficas de respuesta al escalón.  

---

**Autor:** Jesús Salvador López Ortega
[LinkedIn](https://www.linkedin.com/in/jesus-salvador-lopez-ortega/) | [GitHub](https://github.com/chucholoport) | [Correo Institucional](mailto:jlopez@upsrj.edu.mx)
