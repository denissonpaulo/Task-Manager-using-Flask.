import unittest
from todo_project import app, db
from todo_project.models import User

class TaskManagerTestCase(unittest.TestCase):
    def setUp(self):
        # Configura o Flask em modo de teste e usa um banco em memória
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app = app.test_client()
        with app.app_context():
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.drop_all()

    def test_main_page_requires_login_redirect(self):
        # Valida se a rota principal está protegida e redireciona (Requisito de Autenticação)
        response = self.app.get('/all_tasks', follow_redirects=False)
        self.assertEqual(response.status_code, 302)

    def test_login_page_loads(self):
        # Valida se a tela de login está interpretando e renderizando corretamente (Build/Ambiente)
        response = self.app.get('/login')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()