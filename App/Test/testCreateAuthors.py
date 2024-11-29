import unittest
import requests
import time
import concurrent.futures

data = [
  {"id": 1, "name": "JARVIS HUICE"},
  {"id": 2, "name": "ROBERT C MARITN"},
  {"id": 3, "name": "E NAVARRO"},
  {"id": 4, "name": "GOBIERNO BOLIVARIANO DE VENEZUELA"},
  {"id": 5, "name": "MISION SUCRE"},
  {"id": 6, "name": "UBV"},
  {"id": 7, "name": "UNEXCA"},
  {"id": 8, "name": "MARGLEN"},
  {"id": 9, "name": "J. K. ROWLING"},
  {"id": 10, "name": "William Shakespeare"},
  {"id": 11, "name": "Jane Austen"},
  {"id": 12, "name": "Fyodor Dostoevsky"},
  {"id": 13, "name": "Leo Tolstoy"},
  {"id": 14, "name": "Virginia Woolf"},
  {"id": 15, "name": "Franz Kafka"},
  {"id": 16, "name": "Gabriel García Márquez"},
  {"id": 17, "name": "Toni Morrison"},
  {"id": 18, "name": "Haruki Murakami"},
  {"id": 19, "name": "Chimamanda Ngozi Adichie"},
  {"id": 20, "name": "Octavia E. Butler"},
  {"id": 21, "name": "Albert Camus"},
  {"id": 22, "name": "Miguel de Cervantes"},
  {"id": 23, "name": "Dante Alighieri"},
  {"id": 24, "name": "Homer"},
  {"id": 25, "name": "Virgil"},
  {"id": 26, "name": "John Milton"},
  {"id": 27, "name": "Goethe"},
  {"id": 28, "name": "Dostoyevsky"},
  {"id": 29, "name": "Tolstoy"},
  {"id": 30, "name": "Mark Twain"},{"id": 1, "name": "Donald Knuth"},
  {"id": 2, "name": "Edsger Dijkstra"},
  {"id": 3, "name": "Brian Kernighan"},
  {"id": 4, "name": "Dennis Ritchie"},
  {"id": 5, "name": "Thomas H. Cormen"},
  {"id": 6, "name": "Charles E. Leiserson"},
  {"id": 7, "name": "Ronald L. Rivest"},
  {"id": 8, "name": "Clifford Stein"},
  {"id": 9, "name": "Robert Sedgewick"},
  {"id": 10, "name": "Martin Fowler"},
  {"id": 11, "name": "Eric Evans"},
  {"id": 12, "name": "Grady Booch"},
  {"id": 13, "name": "Ralph Johnson"},
  {"id": 14, "name": "Erich Gamma"},
  {"id": 15, "name": "John Vlissides"},
  {"id": 16, "name": "Richard Helm"},
  {"id": 17, "name": "Bjarne Stroustrup"},
  {"id": 18, "name": "Guido van Rossum"},
  {"id": 19, "name": "Stuart Russell"},
  {"id": 20, "name": "Peter Norvig"},
  {"id": 1, "name": "Pitágoras"},
  {"id": 2, "name": "Euclides"},
  {"id": 3, "name": "Arquímedes"},
  {"id": 4, "name": "Isaac Newton"},
  {"id": 5, "name": "Gottfried Leibniz"},
  {"id": 6, "name": "Leonhard Euler"},
  {"id": 7, "name": "Carl Friedrich Gauss"},
  {"id": 8, "name": "Bernhard Riemann"},
  {"id": 9, "name": "David Hilbert"},
  {"id": 10, "name": "Alan Turing"},
  {"id": 11, "name": "Georg Cantor"},
  {"id": 12, "name": "Henri Poincaré"},
  {"id": 13, "name": "Kurt Gödel"},
  {"id": 14, "name": "John von Neumann"},
  {"id": 15, "name": "Emmy Noether"},
  {"id": 16, "name": "Andrew Wiles"},
  {"id": 17, "name": "Grigori Perelman"},
  {"id": 18, "name": "Terence Tao"},
  {"id": 19, "name": "Benoit Mandelbrot"},
  {"id": 20, "name": "Katherine Johnson"},
  {"id": 1, "name": "Isaac Newton"},
  {"id": 2, "name": "Albert Einstein"},
  {"id": 3, "name": "Galileo Galilei"},
  {"id": 4, "name": "Niels Bohr"},
  {"id": 5, "name": "Max Planck"},
  {"id": 6, "name": "Werner Heisenberg"},
  {"id": 7, "name": "Richard Feynman"},
  {"id": 8, "name": "Marie Curie"},
  {"id": 9, "name": "Stephen Hawking"},
  {"id": 10, "name": "James Clerk Maxwell"},
  {"id": 11, "name": "Michael Faraday"},
  {"id": 12, "name": "Erwin Schrödinger"},
  {"id": 13, "name": "Paul Dirac"},
  {"id": 14, "name": "Enrico Fermi"},
  {"id": 15, "name": "Louis Pasteur"},
  {"id": 1, "name": "Charles Darwin"},
  {"id": 2, "name": "Gregor Mendel"},
  {"id": 3, "name": "Louis Pasteur"},
  {"id": 4, "name": "Jane Goodall"},
  {"id": 5, "name": "Francis Crick"},
  {"id": 6, "name": "James Watson"},
  {"id": 7, "name": "Lynn Margulis"},
  {"id": 8, "name": "Carl Linnaeus"},
  {"id": 9, "name": "Barbara McClintock"},
  {"id": 10, "name": "Alexander Fleming"},
  {"id": 11, "name": "Antoine Lavoisier"},
  {"id": 12, "name": "Rachel Carson"},
  {"id": 13, "name": "Rosalind Franklin"},
  {"id": 14, "name": "Ernst Mayr"},
  {"id": 15, "name": "Konrad Lorenz"},
  {"id": 16, "name": "Niko Tinbergen"},
  {"id": 17, "name": "Thomas Hunt Morgan"},
  {"id": 18, "name": "Alfred Russel Wallace"},
  {"id": 19, "name": "Jane Goodall"},
  {"id": 20, "name": "Stephen Jay Gould"},
  {"id": 1, "name": "Isaac Newton"},
  {"id": 2, "name": "Gottfried Leibniz"},
  {"id": 3, "name": "Leonhard Euler"},
  {"id": 4, "name": "Augustin-Louis Cauchy"},
  {"id": 5, "name": "Bernhard Riemann"},
  {"id": 6, "name": "Joseph Fourier"},
  {"id": 7, "name": "Niels Henrik Abel"},
  {"id": 8, "name": "Carl Gustav Jacobi"},
  {"id": 9, "name": "Peter Gustav Lejeune Dirichlet"},
  {"id": 10, "name": "Karl Weierstrass"},
  {"id": 11, "name": "Henri Lebesgue"},
  {"id": 12, "name": "David Hilbert"},
  {"id": 13, "name": "Hermann Weyl"},
  {"id": 14, "name": "John von Neumann"},
  {"id": 15, "name": "Laurent Schwartz"},
  {"id": 16, "name": "Andrey Kolmogorov"},
  {"id": 17, "name": "Lars Hörmander"},
  {"id": 18, "name": "Elias M. Stein"},
  {"id": 19, "name": "Gerardus 't Hooft"},
  {"id": 20, "name": "Edward Witten"},
   {"id": 1, "name": "Antoine Lavoisier"},
  {"id": 2, "name": "Marie Curie"},
  {"id": 3, "name": "Dmitri Mendeleev"},
  {"id": 4, "name": "Linus Pauling"},
  {"id": 5, "name": "Albert Einstein"},
  {"id": 6, "name": "Niels Bohr"},
  {"id": 7, "name": "Friedrich Wöhler"},
  {"id": 8, "name": "Robert Boyle"},
  {"id": 9, "name": "John Dalton"},
  {"id": 10, "name": "Jöns Jacob Berzelius"},
  {"id": 11, "name": "Alfred Nobel"},
  {"id": 12, "name": "Gilbert N. Lewis"},
  {"id": 13, "name": "Otto Hahn"},
  {"id": 14, "name": "Fritz Haber"},
  {"id": 15, "name": "Frederick Sanger"},
  {"id": 16, "name": "Dorothy Hodgkin"},
  {"id": 17, "name": "Glenn Seaborg"},
  {"id": 18, "name": "Kary Mullis"},
  {"id": 19, "name": "Richard Feynman"},
  {"id": 20, "name": "Ada Yonath"},
   {"id": 1, "name": "Eratóstenes de Cirene"},
  {"id": 2, "name": "Claudio Ptolomeo"},
  {"id": 3, "name": "Alexander von Humboldt"},
  {"id": 4, "name": "Carl Ritter"},
  {"id": 5, "name": "Friedrich Ratzel"},
  {"id": 6, "name": "Ellsworth Huntington"},
  {"id": 7, "name": " Vidal de la Blache"},
  {"id": 8, "name": "Walter Christaller"},
  {"id": 9, "name": "Yi-Fu Tuan"},
  {"id": 10, "name": "David Harvey"},
  {"id": 11, "name": "Gilbert White"},
  {"id": 12, "name": "Jared Diamond"},
  {"id": 13, "name": "Michael Watts"},
  {"id": 14, "name": "Neil Smith"},
  {"id": 15, "name": " Doreen Massey"},
  {"id": 16, "name": "Edward Said"},
  {"id": 17, "name": "Henri Lefebvre"},
  {"id": 18, "name": "Manuel Castells"},
  {"id": 19, "name": " Gillian Rose"},
  {"id": 20, "name": "Nigel Thrift"}

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
            self.assertIn(status_code, [200, 400], f"Código de estado inesperado: {status_code}")

        average_response_time = self.total_response_time / self.total_requests
        print(f"Tiempo de respuesta promedio: {average_response_time:.4f} segundos")
        print(f"Total de solicitudes concurrentes manejadas: {self.total_requests}")


    def send_post_request(self, payload):
        start_time = time.time()
        response = requests.post(self.url, json=payload)
        end_time = time.time()

        response_time = end_time - start_time
        status_code = response.status_code
        return payload, response_time, status_code

if __name__ == "__main__":
    unittest.main()
