import locust
import gevent

ENDPOINT_POOL_GET_POST = [
    '/api/authors',
    '/api/labels',
    '/api/genres',
    '/api/labels',
    '/api/playlists',
    '/api/songs',
    '/api/users',
]

class Tester(locust.FastHttpUser):
    @locust.task
    def test(self):
        def con_req(req):
            self.client.get(req, auth=('admin', 'ILoveMother'))
            self.client.get(req+'/1', auth=('admin_mother', 'KillTheChild'))

        pool = gevent.pool.Pool()
        for req in ENDPOINT_POOL_GET_POST:
            pool.spawn(con_req, req)

        pool.join()
