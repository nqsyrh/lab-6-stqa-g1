# API Findings: JSONPlaceholder

Testers (Group 1): Nurul Afiqah Insyirah, Nurul Izzati, Ahmad Zamani, Hanif Aiman
Date: 26 October 2026

Record what the server actually returned for each route. A value
copied from the documentation without being checked against a real
request is not a finding.

## GET /posts/1

| Field        | Value                           |
| ------------ | ------------------------------- |
| Status code  | 200                             |
| Content-Type | application/json; charset=utf-8 |

Response body keys and their types:

| Key    | Type | Example value                                                                |
| ------ | ---- | ---------------------------------------------------------------------------- |
| userId | int  | 1                                                                            |
| id     | int  | 1                                                                            |
| title  | str  | "sunt aut facere repellat provident occaecati excepturi optio reprehenderit" |
| body   | str  | "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum..."      |

## GET /posts

| Field        | Value                           |
| ------------ | ------------------------------- |
| Status code  | 200                             |
| Content-Type | application/json; charset=utf-8 |

Shape of the response body (object or array, and the type of each
element):

A JSON array of 100 elements. Each element is an object with the same
four keys as GET /posts/1: `userId` (int), `id` (int), `title` (str),
`body` (str). The first element is post id 1.

## POST /posts

Request body sent:

```json
{
  "title": "Lab 6 Test",
  "body": "Testing REST API",
  "userId": 1
}
```

| Field        | Value                           |
| ------------ | ------------------------------- |
| Status code  | 201                             |
| Content-Type | application/json; charset=utf-8 |

Response body keys and their types:

| Key    | Type | Example value            |
| ------ | ---- | ------------------------ |
| title  | str  | "Lab 6 Test"             |
| body   | str  | "Testing REST API"       |
| userId | int  | 1                        |
| id     | int  | 101 (added by the server) |

## DELETE /posts/1

| Field        | Value                           |
| ------------ | ------------------------------- |
| Status code  | 200                             |
| Content-Type | application/json; charset=utf-8 |

Response body:

`{}` (an empty JSON object)

## Notes

- Content-Type for every route is `application/json; charset=utf-8`,
  not plain `application/json` as used in Part 1.
- GET /posts/1 returned a JSON object containing `userId`, `id`, `title`, and `body`.
- GET /posts returned a JSON array containing 100 post objects.
- POST /posts returned status code 201 and the server added a new `id` value of 101.
- DELETE /posts/1 returned status code 200 with an empty JSON object `{}`.
- Conclusion: The API returned the expected success responses for all four routes tested. This shows that API testing should check not only the status code, but also the response headers and the structure of the response body.
