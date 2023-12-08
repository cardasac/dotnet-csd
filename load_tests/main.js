import { sleep } from 'k6'
import http from 'k6/http'

// See https://k6.io/docs/using-k6/options
export const options = {
  stages: [
    { duration: '1m', target: 20 }
  ],
  thresholds: {
    http_req_failed: ['rate<0.01'], // http errors should be less than 1%
    http_req_duration: ['p(99.9)<50'], // 99.9% requests should be below 50ms
  },
  ext: {
    loadimpact: {
      distribution: {
        'amazon:ie:dublin': { loadZone: 'amazon:ie:dublin', percent: 100 }
      },
    },
  },
}

export default function main() {
  http.get(`https://${__ENV.APP_HOSTNAME}/`)
  sleep(1)
}