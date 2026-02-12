# Práctica: Diseño de realimentación para cumplir requisitos de descarga en un sistema RC
## Contexto industrial
Estás diseñando un sistema de adquisición de señales para una planta de manufactura. La señal analógica pasa por un filtro RC con realimentación resistiva antes de ser digitalizada. El sistema debe cumplir con un requisito de tiempo de descarga para evitar interferencias entre muestras consecutivas.
Tu fuente de alimentación entrega 5 V con una corriente máxima de 10 mA, y los componentes disponibles en almacén incluyen resistencias estándar (E12) y capacitores cerámicos de bajo costo.

## Objetivo
Determinar el valor adecuado de la resistencia de realimentación  para que el sistema cumpla con un tiempo de establecimiento especificado, sin exceder las limitaciones de corriente ni usar componentes no disponibles.

## Fundamento teórico
La función de transferencia del circuito RC con realimentación es:

![transfer_function](https://quicklatex.com/cache3/76/ql_f30c214387d547ff185501bdef008e76_l3.png)

El polo del sistema está en:

![polo](https://quicklatex.com/cache3/c4/ql_19f7bbf013ecb31773d787a5011e0ac4_l3.png)

Y el tiempo de establecimiento aproximado es:

![ts](https://quicklatex.com/cache3/87/ql_0927b8e211bc4211536a1225f930de87_l3.png)

## Actividad
1. Investiga qué valores de `R` y `C` puedes usar sin exceder los 10 mA de corriente con 5 V.

    - Recuerda que ![kirchoff](https://quicklatex.com/cache3/72/ql_0252f7079036deefdc19e695e0b8f972_l3.png)
    - Ejemplo: ![R](https://quicklatex.com/cache3/49/ql_39f78b994a50247aa89541bb8fe7cb49_l3.png) → ![I](https://quicklatex.com/cache3/37/ql_4f42a3e11e713ac95b8a40059ef1cd37_l3.png) 

2. Calcula el polo deseado para un tiempo de establecimiento `ts=0.1s`, `ts=0.2s`, `ts=0.3s`:
   
    ![sd](https://quicklatex.com/cache3/86/ql_ee865a6a9eb38dcc1311121f381d9286_l3.png)

3. Despeja :
   
    ![rf](https://quicklatex.com/cache3/c6/ql_bcdd819f9395a2faff7e2b7e1960e0c6_l3.png)

4. Implementa la función de transferencia en `rc_feedback(R, C, Rf)` dentro de `control_system/plant.py`:
   
    ![transfer_function](https://quicklatex.com/cache3/76/ql_f30c214387d547ff185501bdef008e76_l3.png)

5. Simula la respuesta al escalón con los distintos tiempos de establecimiento `ts=0.1s`, `ts=0.2s`, `ts=0.3s`.
   - Genera una gráfica por cada caso.
   - Las tres gráficas deben estar en `build/out`.

6. Registra los resultados en `build/out/register.csv` mediante `add_entry(R, C, Rf, ts, pole)`

7. Valida que el sistema cumple con el requisito observando las gráficas de respuesta al escalón.