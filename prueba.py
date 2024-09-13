import pybullet as p
import tensorflow as tf
import os

def main():
    try:
        # Establecer la variable de entorno para oneDNN si se desea desactivar
        os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

        # Configuración inicial de TensorFlow
        print("Versión de TensorFlow:", tf.__version__)

        # Inicializar PyBullet
        print("Inicializando PyBullet...")
        physicsClient = p.connect(p.GUI)
        
        # Realizar operaciones con PyBullet
        print("Configurando el entorno...")
        p.setGravity(0, 0, -9.8)
        p.loadURDF("plane.urdf")

        # Realizar una simulación simple
        print("Ejecutando simulación...")
        for _ in range(240):  # 240 pasos de simulación
            p.stepSimulation()

        # Desconectar PyBullet
        p.disconnect()

        print("Simulación completa.")

    except Exception as e:
        print(f"Se ha producido un error: {e}")
    
    finally:
        input("Presiona Enter para cerrar...")

if __name__ == "__main__":
    main()
