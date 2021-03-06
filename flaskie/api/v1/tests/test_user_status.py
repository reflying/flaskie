import json
from .base_test import BaseTestCase

class TestUserStatus(BaseTestCase):
    def test_user_status(self):
        with self.client:
            resp_register = self.client.post(
                '/api/v1/auth/register',
                data=json.dumps(dict(
                    name='Chessi Mboya',
                    email='chessi@gmail.com',
                    username='chessi',
                    password='mermaid'
                )),
                content_type='application/json'
            )
            response = self.client.get(
                '/api/v1/user',
                headers=dict(
                    Authorization='Bearer ' + json.loads(
                        resp_register.data.decode()
                    )['Authorization']['access_token']
                )
            )
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 'success')
            self.assertTrue(data['data'] is not None)
            self.assertTrue(data['data']['email'] == 'chessi@gmail.com')
            self.assertTrue(data['data']['admin'] is 'true' or 'false')
            self.assertEqual(response.status_code, 200)

    def test_user_can_change_their_profile(self):
        with self.client:
            resp_register = self.client.post(
                '/api/v1/auth/login',
                data=json.dumps(dict(
                    username='paulla',
                    password='mermaid'
                )),
                content_type='application/json'
            )
            print(resp_register)
            response = self.client.put(
                '/api/v1/user/paulla000',
                headers=dict(
                    Authorization='Bearer ' + json.loads(
                        resp_register.data.decode()
                    )['Authorization']['access_token']
                ),
                data=json.dumps(dict(
                    name='Faith Mboya',
                    email='mermaid@gmail.com',
                    username='mermaid',
                    password='mermaid'
                )),
                content_type='application/json'
            )
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 'success')
            self.assertTrue(data['message'] == 'user updated successfully')
            self.assertEqual(response.status_code, 200)