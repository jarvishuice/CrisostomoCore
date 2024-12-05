import unittest
import requests
import time
import concurrent.futures

data = [
  {"id": 1, "name": "JARVIS HUICE", "description": "no posee description"},
  {"id": 2, "name": "ROBERT C MARITN", "description": "no posee description"},
  {"id": 3, "name": "E NAVARRO", "description": "no posee description"},
  {"id": 4, "name": "GOBIERNO BOLIVARIANO DE VENEZUELA", "description": "no posee description"},
  {"id": 5, "name": "MISION SUCRE", "description": "no posee description"},
  {"id": 6, "name": "UBV", "description": "no posee description"},
  {"id": 7, "name": "UNEXCA", "description": "no posee description"},
  {"id": 8, "name": "MARGLEN", "description": "no posee description"},
  {"id": 9, "name": "J. K. ROWLING", "description": "Autora británica conocida por su serie de libros de fantasía que ha cautivado a millones de lectores en todo el mundo. Su estilo narrativo y la construcción de personajes han dejado una huella indeleble en la literatura contemporánea. Mejores trabajos: 'Harry Potter y la piedra filosofal', 'Harry Potter y las reliquias de la muerte'."},
  {"id": 10, "name": "William Shakespeare", "description": "Dramaturgo y poeta inglés, considerado uno de los más grandes escritores de la lengua inglesa. Sus obras abordan temas universales como el amor, la ambición y la traición, y han sido traducidas a numerosos idiomas. Mejores trabajos: 'Hamlet', 'Romeo y Julieta', 'Macbeth'."},
  {"id": 11, "name": "Jane Austen", "description": "Novelista inglesa que exploró la vida de las mujeres en la sociedad del siglo XIX a través de su ingenio y aguda observación social. Sus obras son conocidas por su crítica a las normas sociales de su tiempo. Mejores trabajos: 'Orgullo y prejuicio', 'Sentido y sensibilidad'."},
  {"id": 12, "name": "Fyodor Dostoevsky", "description": "Novelista ruso cuyas obras exploran la psicología humana y los dilemas morales. Su estilo introspectivo y su enfoque en la lucha entre el bien y el mal han influido en la literatura moderna. Mejores trabajos: 'Crimen y castigo', 'Los hermanos Karamazov'."},
  {"id": 13, "name": "Leo Tolstoy", "description": "Novelista ruso conocido por su profunda exploración de la condición humana y su crítica a la sociedad. Sus obras abordan temas de amor, guerra y la búsqueda de la verdad. Mejores trabajos: 'Guerra y paz', 'Anna Karenina'."},
  {"id": 14, "name": "Virginia Woolf", "description": "Escritora británica y pionera del modernismo literario, conocida por su estilo innovador y su enfoque en la subjetividad. Sus obras a menudo exploran la vida interior de sus personajes. Mejores trabajos: 'La señora Dalloway', 'Al faro'."},
  {"id": 15, "name": "Franz Kafka", "description": "Escritor checo conocido por sus obras surrealistas y existencialistas que exploran la alienación y la burocracia. Su estilo único ha influido en la literatura del siglo XX. Mejores trabajos: 'La metamorfosis', 'El proceso'."},
  {"id": 16, "name": "Gabriel García Márquez", "description": "Novelista colombiano, ganador del Premio Nobel, conocido por su estilo de realismo mágico que combina lo fantástico con lo cotidiano. Sus obras han tenido un impacto significativo en la literatura latinoamericana. Mejores trabajos: 'Cien años de soledad', 'El amor en los tiempos del cólera'."},
  {"id": 17, "name": "Toni Morrison", "description": "Novelista estadounidense, ganadora del Premio Nobel, cuyas obras abordan la experiencia afroamericana y la identidad racial. Su estilo lírico y su enfoque en la historia han resonado en la literatura contemporánea. Mejores trabajos: 'Beloved', 'Song of Solomon'."},
  {"id": 18, "name": "Haruki Murakami", "description": "Novelista japonés conocido por su estilo surrealista y su exploración de la soledad y la búsqueda de identidad. Sus obras a menudo combinan elementos de la cultura pop con la filosofía. Mejores trabajos: 'Kafka en la orilla', '1Q84'."},
  {"id": 19, "name": "Chimamanda Ngozi Adichie", "description": "Escritora nigeriana cuyas obras abordan temas de identidad, feminismo y la experiencia africana. Su estilo narrativo y su enfoque en la diversidad cultural han sido aclamados internacionalmente. Mejores trabajos: 'Medio sol amarillo', 'Americanah'."},
  {"id": 20, "name": "Octavia E. Butler", "description": "Autora de ciencia ficción estadounidense, conocida por su enfoque en temas de raza, género y poder. Su trabajo ha desafiado las convenciones del género y ha abierto nuevas vías para la narrativa. Mejores trabajos: 'Kindred', 'Parable of the Sower'."},
  {"id": 21, "name": "Albert Camus", "description": "Filósofo y escritor francés, conocido por su exploración del absurdo y la condición humana. Su obra ha influido en la filosofía existencialista y en la literatura contemporánea. Mejores trabajos: 'El extranjero', 'La peste'."},
  {"id": 22, "name": "Miguel de Cervantes", "description": "Novelista español, considerado el padre de la novela moderna. Su obra ha tenido un impacto duradero en la literatura y la cultura occidental. Mejores trabajos: 'Don Quijote de la Mancha'."},
  {"id": 23, "name": "Dante Alighieri", "description": "Poeta italiano, conocido por su obra maestra 'La Divina Comedia', que explora la vida después de la muerte y la búsqueda de la redención. Su trabajo ha influido en la literatura y la teología. Mejores trabajos: 'La Divina Comedia'."},
  {"id": 24, "name": "Homer", "description": "Poeta griego antiguo, autor de las epopeyas 'La Ilíada' y 'La Odisea', que han sido fundamentales en la literatura occidental. Su trabajo ha influido en la narrativa y la poesía a lo largo de los siglos. Mejores trabajos: 'La Ilíada', 'La Odisea'."},
  {"id": 25, "name": "Virgil", "description": "Poeta romano, conocido por su obra 'La Eneida', que narra la historia de Eneas y su viaje a Italia. Su trabajo ha tenido un impacto significativo en la literatura y la cultura romana. Mejores trabajos: 'La Eneida'."},
  {"id": 26, "name": "John Milton", "description": "Poeta inglés, conocido por su obra 'El paraíso perdido', que explora temas de la caída del hombre y la redención. Su estilo y contenido han influido en la poesía y la literatura religiosa. Mejores trabajos: 'El paraíso perdido'."},
  {"id": 27, "name": "Goethe", "description": "Escritor y filósofo alemán, conocido por su obra 'Fausto', que explora la búsqueda del conocimiento y la lucha entre el bien y el mal. Su trabajo ha influido en la literatura y la filosofía. Mejores trabajos: 'Fausto'."},
  {"id": 28, "name": "Dostoyevsky", "description": "no posee description"},
  {"id": 29, "name": "Tolstoy", "description": "no posee description"},
  {"id": 30, "name": "Mark Twain", "description": "Novelista estadounidense, conocido por su aguda crítica social y su estilo humorístico. Sus obras han explorado la vida en América y la lucha por la libertad. Mejores trabajos: 'Las aventuras de Tom Sawyer', 'Las aventuras de Huckleberry Finn'."},
  {"id": 1, "name": "Donald Knuth", "description": "Informático estadounidense, conocido por su trabajo en algoritmos y su enfoque en la programación. Su obra ha establecido estándares en el campo de la informática. Mejores trabajos: 'The Art of Computer Programming'."},
  {"id": 2, "name": "Edsger Dijkstra", "description": "Informático neerlandés, conocido por sus contribuciones a la teoría de algoritmos y la programación estructurada. Su trabajo ha influido en la forma en que se desarrollan los programas de software. Mejores trabajos: 'Algoritmos de Dijkstra'."},
  {"id": 3, "name": "Brian Kernighan", "description": "Informático canadiense, coautor de 'The C Programming Language' y conocido por su trabajo en el desarrollo de Unix. Su influencia se extiende a la educación en programación. Mejores trabajos: 'The C Programming Language'."},
  {"id": 4, "name": "Dennis Ritchie", "description": "Informático estadounidense, co-creador del lenguaje C y del sistema operativo Unix. Su trabajo ha sido fundamental en el desarrollo de la programación moderna. Mejores trabajos: 'Lenguaje C', 'Unix'."},
  {"id": 5, "name": "Thomas H. Cormen", "description": "Informático estadounidense, coautor de 'Introduction to Algorithms', un texto fundamental en el estudio de algoritmos. Su trabajo ha sido influyente en la educación en informática. Mejores trabajos: 'Introduction to Algorithms'."},
  {"id": 6, "name": "Charles E. Leiserson", "description": "Informático estadounidense, coautor de 'Introduction to Algorithms' y conocido por su trabajo en la teoría de algoritmos. Su investigación ha impactado en el campo de la informática. Mejores trabajos: 'Introduction to Algorithms'."},
  {"id": 7, "name": "Ronald L. Rivest", "description": "Informático estadounidense, conocido por su trabajo en criptografía y coautor de 'Introduction to Algorithms'. Su investigación ha sido fundamental en la seguridad informática. Mejores trabajos: 'Introduction to Algorithms'."},
  {"id": 8, "name": "Clifford Stein", "description": "Informático estadounidense, conocido por su trabajo en algoritmos y coautor de 'Introduction to Algorithms'. Su investigación ha influido en el desarrollo de algoritmos eficientes. Mejores trabajos: 'Introduction to Algorithms'."},
  {"id": 9, "name": "Robert Sedgewick", "description": "Informático estadounidense, autor de varios libros sobre algoritmos y estructuras de datos. Su trabajo ha sido fundamental en la educación en informática. Mejores trabajos: 'Algorithms', 'Algorithms in C'."},
  {"id": 10, "name": "Martin Fowler", "description": "Autor y consultor en desarrollo de software, conocido por su trabajo en refactorización y patrones de diseño. Su enfoque ha influido en la práctica del desarrollo ágil. Mejores trabajos: 'Refactoring', 'Patterns of Enterprise Application Architecture'."},
  {"id": 11, "name": "Eric Evans", "description": "Autor de 'Domain-Driven Design', un enfoque para el desarrollo de software que enfatiza la colaboración entre expertos en el dominio y desarrolladores. Su trabajo ha sido influyente en la arquitectura de software. Mejores trabajos: 'Domain-Driven Design'."},
  {"id": 12, "name": "Grady Booch", "description": "Informático estadounidense, conocido por su trabajo en ingeniería de software y el desarrollo de UML. Su enfoque ha sido fundamental en la modelización de sistemas. Mejores trabajos: 'Object-Oriented Analysis and Design'."},
  {"id": 13, "name": "Ralph Johnson", "description": "Informático estadounidense, conocido por su trabajo en patrones de diseño y coautor de 'Design Patterns'. Su investigación ha influido en la programación orientada a objetos. Mejores trabajos: 'Design Patterns'."},
  {"id": 14, "name": "Erich Gamma", "description": "Informático, coautor de 'Design Patterns' y conocido por sus contribuciones a la programación orientada a objetos. Su trabajo ha sido fundamental en el desarrollo de software. Mejores trabajos: 'Design Patterns'."},
  {"id": 15, "name": "John Vlissides", "description": "Informático, coautor de 'Design Patterns' y conocido por su trabajo en programación orientada a objetos. Su investigación ha influido en la práctica del desarrollo de software. Mejores trabajos: 'Design Patterns'."},
  {"id": 16, "name": "Richard Helm", "description": "Informático, coautor de 'Design Patterns' y conocido por su trabajo en programación orientada a objetos. Su investigación ha sido fundamental en el desarrollo de software. Mejores trabajos: 'Design Patterns'."},
  {"id": 17, "name": "Bjarne Stroustrup", "description": "Creador del lenguaje de programación C++ y autor de 'The C++ Programming Language'. Su trabajo ha influido en el desarrollo de software y la programación orientada a objetos. Mejores trabajos: 'The C++ Programming Language'."},
  {"id": 18, "name": "Guido van Rossum", "description": "Creador del lenguaje de programación Python, conocido por su enfoque en la simplicidad y la legibilidad del código. Su trabajo ha tenido un impacto significativo en la programación moderna. Mejores trabajos: 'Python Programming'."},
  {"id": 19, "name": "Stuart Russell", "description": "Investigador en inteligencia artificial, coautor de 'Artificial Intelligence: A Modern Approach'. Su trabajo ha sido fundamental en el desarrollo de la IA moderna. Mejores trabajos: 'Artificial Intelligence: A Modern Approach'."},
  {"id": 20, "name": "Peter Norvig", "description": "Investigador en inteligencia artificial y director de investigación en Google. Su trabajo ha influido en el desarrollo de algoritmos y sistemas de IA. Mejores trabajos: 'Artificial Intelligence: A Modern Approach'."},
  {"id": 1, "name": "Pitágoras", "description": "Filósofo y matemático griego, conocido por su teorema que relaciona los lados de un triángulo rectángulo. Su trabajo ha influido en la matemática y la filosofía. Mejores trabajos: Teorema de Pitágoras."},
  {"id": 2, "name": "Euclides", "description": "Matemático griego, conocido como el 'padre de la geometría'. Su obra 'Los Elementos' ha sido fundamental en la enseñanza de la geometría. Mejores trabajos: 'Los Elementos'."},
  {"id": 3, "name": "Arquímedes", "description": "Matemático y físico griego, conocido por sus principios de palanca y flotación. Su trabajo ha influido en la física y la ingeniería. Mejores trabajos: Principios de Arquímedes."},
  {"id": 4, "name": "Isaac Newton", "description": "Físico y matemático inglés, conocido por sus leyes del movimiento y la ley de la gravitación universal. Su trabajo ha sido fundamental en la física clásica. Mejores trabajos: 'Philosophiæ Naturalis Principia Mathematica'."},
  {"id": 5, "name": "Gottfried Leibniz", "description": "Filósofo y matemático alemán, co-inventor del cálculo. Su trabajo ha influido en la matemática y la filosofía moderna. Mejores trabajos: 'Calculus'."},
  {"id": 6, "name": "Leonhard Euler", "description": "Matemático suizo, conocido por sus contribuciones a la matemática y la física. Su trabajo ha influido en diversas áreas de la matemática. Mejores trabajos: 'Introductio in analysin infinitorum'."},
  {"id": 7, "name": "Carl Friedrich Gauss", "description": "Matemático alemán, conocido por sus contribuciones a la teoría de números y la estadística. Su trabajo ha sido fundamental en la matemática moderna. Mejores trabajos: 'Disquisitiones Arithmeticae'."},
  {"id": 8, "name": "Bernhard Riemann", "description": "Matemático alemán, conocido por su trabajo en análisis y la hipótesis de Riemann. Su investigación ha influido en la teoría de números y la geometría. Mejores trabajos: 'Über die Hypothesen, welche der Geometrie zu Grunde liegen'."},
  {"id": 9, "name": "David Hilbert", "description": "Matemático alemán, conocido por sus problemas de Hilbert y su trabajo en lógica y matemáticas. Su influencia ha sido fundamental en el desarrollo de la matemática moderna. Mejores trabajos: 'Grundlagen der Geometrie'."},
  {"id": 10, "name": "Alan Turing", "description": "Matemático y lógico británico, considerado el padre de la computación moderna. Su trabajo ha influido en la teoría de la computación y la inteligencia artificial. Mejores trabajos: 'On Computable Numbers'."},
  {"id": 11, "name": "Georg Cantor", "description": "Matemático alemán, conocido por su trabajo en teoría de conjuntos y la noción de infinito. Su investigación ha influido en la matemática moderna. Mejores trabajos: 'Grundlagen einer allgemeinen Mannigfaltigkeitslehre'."},
  {"id": 12, "name": "Henri Poincaré", "description": "Matemático y físico francés, conocido por sus contribuciones a la topología y la teoría del caos. Su trabajo ha influido en la matemática y la física moderna. Mejores trabajos: 'Science and Hypothesis'."},
  {"id": 13, "name": "Kurt Gödel", "description": "Lógico y matemático austriaco, conocido por sus teoremas de incompletitud. Su trabajo ha tenido un impacto significativo en la lógica y la filosofía. Mejores trabajos: 'On Formally Undecidable Propositions'."},
  {"id": 14, "name": "John von Neumann", "description": "Matemático y físico húngaro, conocido por sus contribuciones a la teoría de juegos y la computación. Su trabajo ha influido en la matemática y la economía. Mejores trabajos: 'Theory of Games and Economic Behavior'."},
  {"id": 15, "name": "Emmy Noether", "description": "Matemática alemana, conocida por su trabajo en álgebra abstracta y teoría de invariantes. Su investigación ha sido fundamental en la matemática moderna. Mejores trabajos: 'Noether's Theorem'."},
  {"id": 16, "name": "Andrew Wiles", "description": "Matemático británico, conocido por demostrar el último teorema de Fermat. Su trabajo ha sido un hito en la teoría de números. Mejores trabajos: 'Modular Elliptic Curves and Fermat's Last Theorem'."},
  {"id": 17, "name": "Grigori Perelman", "description": "Matemático ruso, conocido por resolver la conjetura de Poincaré. Su trabajo ha sido fundamental en la topología. Mejores trabajos: 'The Entropy Formula for the Ricci Flow and the Poincaré Conjecture'."},
  {"id": 18, "name": "Terence Tao", "description": "Matemático australiano, conocido por sus contribuciones a análisis, teoría de números y combinatoria. Su trabajo ha influido en diversas áreas de la matemática. Mejores trabajos: 'Solving the Navier-Stokes Existence and Smoothness Problem'."},
  {"id": 19, "name": "Benoit Mandelbrot", "description": "Matemático y científico, conocido por su trabajo en geometría fractal y la teoría del caos. Su investigación ha influido en la matemática y la ciencia. Mejores trabajos: 'The Fractal Geometry of Nature'."},
  {"id": 20, "name": "Katherine Johnson", "description": "Matemática y física estadounidense, conocida por su trabajo en cálculos orbitales para la NASA. Su contribución fue fundamental para el éxito de las misiones espaciales. Mejores trabajos: Cálculos para el vuelo de John Glenn."}
]
class TestCreateAuthors(unittest.TestCase):

    def setUp(self):
        self.url = "http://localhost:8091/API/Author/create"
        self.payloads = data
        self.total_response_time = 0
        self.total_requests = len(data)
    
    def test_parallel_requests(self):
        with concurrent.futures.ThreadPoolExecutor(max_workers=self.total_requests) as executor:
            futures = [executor.submit(self.send_post_request, payload) for payload in self.payloads]
            results = [f.result() for f in concurrent.futures.as_completed(futures)]
        
        for result in results:
            payload, response_time, status_code = result
            self.total_response_time += response_time
            print(f"Payload: {payload}, Tiempo de respuesta: {response_time:.4f} segundos, Código de estado: {status_code}")
            self.assertIn(status_code, [200, 400,500], f"Código de estado inesperado: {status_code}")

        average_response_time = self.total_response_time / self.total_requests
        print(f"Tiempo de respuesta promedio: {average_response_time:.4f} segundos")
        print(f"Total de solicitudes concurrentes manejadas: {self.total_requests}")


    def send_post_request(self, payload):
        start_time = time.time()
        try:
            # Imprimir la descripción antes de enviar la solicitud
            print(f"Enviando: {payload['name']} - Descripción: {payload['description']}")
            response = requests.post(self.url, json=payload)
            response.raise_for_status()  # Lanza un error para códigos de estado 4xx/5xx
        except requests.exceptions.RequestException as e:
            print(f"Error en la solicitud: {e}")
            return payload, 0, 500  # Código de estado 500 para errores de conexión
        end_time = time.time()

        response_time = end_time - start_time
        status_code = response.status_code
        return payload, response_time, status_code

if __name__ == "__main__":
    unittest.main()
