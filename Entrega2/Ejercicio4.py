evaluar = """ título: Experiences in Developing a Distributed Agent-based
Modeling Toolkit with Python
resumen: Distributed agent-based modeling (ABM) on high-performance
computing resources provides the promise of capturing unprecedented details
of large-scale complex systems. However, the specialized knowledge required
for developing such ABMs creates barriers to wider adoption and utilization.
Here we present our experiences in developing an initial implementation of
Repast4Py, a Python-based distributed ABM toolkit. We build on our
experiences in developing ABM toolkits, including Repast for High
Performance Computing (Repast HPC), to identify the key elements of a useful
distributed ABM toolkit. We leverage the Numba, NumPy, and PyTorch packages
and the Python C-API to create a scalable modeling system that can exploit
the largest HPC resources and emerging computing architectures.
"""
evaluar = evaluar.replace("título:", "").split("resumen: ")
titulo = evaluar[0].split()
resumen = evaluar[1].replace("\n", " ").split(".")
resumen.pop()
print(resumen)
ok = False
cantFacil = 0
cantAceptable = 0
cantDificil = 0
cantMuyDificil = 0
if len(titulo) <= 10:
    ok = True
for i in resumen:
    largo = len(i.split())
    if largo <= 12:
        cantFacil += 1
    else:
        if largo <= 17:
            cantAceptable +=1
        else:
            if largo <= 25:
                cantDificil += 1
            else:
                cantMuyDificil +=1

print(f"titulo: {ok}")
print(f"Cantidad de oraciones fáciles de leer: {cantFacil}")
print(f"aceptables para leer: {cantAceptable}")
print(f"dificil de leer: {cantDificil}")
print(f"muy dificil de leer: {cantMuyDificil}")

