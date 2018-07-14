# Working Incrementally

- New feature? Write a new functional test.
- But don't design a big feature, make it small and easily testable.
- Think of the _Minimum Viable Product_ (MVP) - what is the least amount of features to get the job done.

## YAGNI!

> _You aren't gonna need it!_

- This goes hand in hand with the previous point: a lot of features are great, but do you really need it? Make it work first then add on it once you're confident and well tested

## Using REST(ish)

- Entities are represented as `Models` in the MVC. How about the interaction of the `Controller` (views in Django) and `Views` (templates)? We could follow the REST design for this.

| HTTP Verb | URL                     | Description                               | Alias     |
| --------- | ----------------------- | ----------------------------------------- | --------- |
| GET       | `/resource`             | Show all the resources                    | `index`   |
| POST      | `/resource`             | Create a new resource                     | `store`   |
| GET       | `/resource/new`         | Show the form for creating a new resource | `create`  |
| GET       | `/resource/<id>`        | Show a specific resource                  | `show`    |
| GET       | `/resource/<id>/edit`   | Show the form for editing a resource      | `edit`    |
| PATCH     | `/resource/<id>`        | Edit the resource data                    | `update`  |
| DELETE    | `/resource/<id>`        | Delete the resource                       | `destroy` |
| <VERB>    | `/resource/<id>/<verb>` | Connects the resource to another          | --------- |
