from django.test import TestCase
from django.urls import reverse
from .models import Task

# Create your tests here.
class TaskModelTests(TestCase):
    def test_str_representation(self):
        task = Task.objects.create(title='Test Task')
        self.assertEqual(str(task), 'Test Task')

    def test_str_representation2(self):
        task = Task.objects.create(title='asdkjfajskdfjljlkajdkfljlasdkfjlk')
        self.assertEqual(str(task), 'asdkjfajskdfjljlkajdkfljlasdkfjlk')

class TaskViewTests(TestCase):
    def test_task_list_view(self):
        response = self.client.get(reverse('task_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'TodoApp/task_list.html')

    def test_task_detail_view(self):
        task = Task.objects.create(title="test1")
        response = self.client.get(reverse('task_detail'), args=(task.id, ))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'TodoApp/task_detail.html')
        self.assertContains(response, 'test1')

    def test_task_create_view(self):
        response = self.client.get(reverse('task_create')) # 이 페이지를 가져옴
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'TodoApp/create_task.html')

        data = {
            'title': 'test2'
        }
        response = self.client.post(reverse('task_create'), data) # 지금은 데이터를 보내봄
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Task.objects.cunt(), 1)
    
    def test_task_update_view(self):
        task = Task.objects.create(title="test3")
        response = self.client.get(reverse('task_update', args=(task.pk, )))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'TodoApp/task_update.html')

        # 컨텐츠까지 확인을 원하면?
        self.assertEqual(task.title, 'test3')

        # 업데이트 수행
        updated_data = {
            'title' : 'Update Task'
        }

        response = self.client.post(reverse('task_update', args=(task.pk, )), updated_data)
        # 전달될 데이터가 잘 반영되었는지 확인
        self.assertEqual(response.status_code, 302)

        # DB로부터 task 내용을 재갱신
        task.refresh_from_db()
        self.assertEqual(task.title, 'Update Task')

def test_task_delete_view(self):
    task = Task.objects.create(title='test Task')
    self.assertEqual(Task.objects.count(), 1)

    response = self.client.post(reverse('task_delete', args=(task.pk, )))
    self.assertEqual(response.status_code, 302)
    self.assertEqual(Task.objects.count(), 0)


