import { sleep } from 'k6'
import http from 'k6/http'

// See https://k6.io/docs/using-k6/options
export const options = {
  stages: [
    { duration: '1m', target: 20 }
  ],
  thresholds: {
    http_req_failed: ['count=0'], // http errors should be less than 1%
    http_req_duration: ['p(99.9)<20'], // 99.9% requests should be below 20ms
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
  http.get(`http://${__ENV.APP_HOSTNAME}/`)
  sleep(1)
}