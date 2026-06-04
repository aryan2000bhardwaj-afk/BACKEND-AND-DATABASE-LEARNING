import Tasks from "../models/task.js";
import dotenv from 'dotenv';
import jwt from 'jsonwebtoken';

dotenv.config();

const SECRETE_KEY = process.env.SECRETE_KEY;

export async function createTask(data, token) {
        console.log("DATA:", data);
    console.log("TOKEN:", token);
    try {
        const payload = jwt.verify(token, SECRETE_KEY);
        data.createdby =  payload.crid;
        await Tasks.create(data);
        return {code: 200, message: "New task has been created"};
    } catch (error) {
        return {code: 500, message: error.message};
    }
}