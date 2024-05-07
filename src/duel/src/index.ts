
let id: number = 5
let company: string = "Repair Man Industries"
let isPublished: boolean = false
let x: any = "sex"


let age: number
age = 31

let ids: number[] = [1,2,3,4]
let anyArray: any[] = [1, 2, "string"]

let person: [number, string, boolean, number[]] = [1, 'Saxophone', true, [1, 2, 3]]
let employee: [number, string][]

employee = [
    [1, "Jacob"],
    [2, "Kay"],
    [3, "Jane"]
]

let employee2: []


let pid: string | number
pid = 'hi'
pid = 22

enum Direction1 {
    Up = "up",
    Down ="down",
    Left = "left",
    Right = 'right'
}

// console.log(Direction1.Up)

type User = {
    id: number,
    name: string
}

const user1: {
    id: number,
    name: string
} = {
    id: 1,
    name: 'John'
}


const user2: User = {
    id: 123,
    name: 'Jake',
}

// Type assertion

let cid: any = 1
let customerId1 = <number>cid
let customerId2 = cid as number
