import http from 'k6/http';
import { check  } from 'k6';

export let options = {
    vus: 10,
    duration: '30s',
};

export default function () {
    let res = http.get('https://example.com');
    check(res, {
        'status is 200': (r) => r.status === 200,
    });
}
