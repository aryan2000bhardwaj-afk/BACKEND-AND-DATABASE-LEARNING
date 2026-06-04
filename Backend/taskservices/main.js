import express from 'express';
import cors from 'cors';
import dotenv from 'dotenv';
import taskRouter from './controllers/taskControllers.js';
import { connectDB } from './config/db.js';

dotenv.config();

const app = express();

app.use(express.json());
app.use(cors());

connectDB();

app.use("/task", taskRouter);

app.get("/", (req, res) => {
    res.json({
        code: 200,
        message: "Started...."
    });
});

const PORT = process.env.PORT || 5000;

app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
});