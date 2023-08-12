src/index.ts
============

Last edited: 2020-09-25 20:09:31

Contents:

.. code-block:: ts

    import http from "http"
import fetch from "node-fetch"

//@ts-ignore
import { endpoints, port } from "../config.json"

const server = http
    .createServer((req: http.IncomingMessage, res: http.ServerResponse) => {
        const { method } = req

        let data: Uint8Array[] = [];

        req.on("data", (chunk: any) => {
            data.push(chunk)
        }).on("end", () => {        
            const payload = Buffer.concat(data).toString(); 
            data = []   

            endpoints.forEach((endpoint) => {
                fetch(endpoint, { method, body: payload })
                    .then((r: any) => {
                        console.log(
                            `${endpoint} ${r.status} ${r.statusText} x-request-id=${r.headers.get(
                                "x-request-id"
                            )} x-influxdb-build=${r.headers.get(
                                "x-influxdb-build"
                            )} x-influxdb-version=${r.headers.get(
                                "x-influxdb-version"
                            )} x-influxdb-error=${r.headers.get("x-influxdb-error")}`
                        )
                    })
                    .catch((error) => {
                        console.log(error)
                    })
            })
        })

        res.writeHead(200)
        res.end()
    })
    .listen(port)

server.setMaxListeners(20)

console.log(`Server running at http://127.0.0.1:${port}/`)


