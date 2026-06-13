import express from 'express'
import * as taskService from '../services/taskservice.js'  // ✅ Fixed import


const router = express.Router();

router.post("/createtask",async(req,res)=>{
    res.json(await taskService.createTask(req.body,req.headers["token"]));
})


router.get("/getalltasks/:PAGE/:SIZE", async (req, res) => {
    const { PAGE, SIZE } = req.params;
    res.json(await taskService.getAllTasks(PAGE, SIZE, req.headers["token"]));
});


router.delete("/deletetask/:ID", async (req, res)=>{
    const {ID} = req.params;
    const response = await taskService.deleteTask(ID, req.headers["token"]);
    res.json(response);
});



router.get("/gettask/:ID", async(req, res) => {
    const { ID } = req.params;
    const response = await taskService.getTask(ID, req.headers["token"]);  // ✅ Fixed: was taskServices
    res.json(response);
});


router.put("/updatetask/:ID", async (req, res) => {
    const { ID } = req.params;
    const response = await taskService.updateTask(ID, req.body, req.headers["token"]);
    res.json(response);
});


router.get("/vectorsearch/:QUERY", async (req, res)=>{
    const {QUERY} = req.params;
    const response = await taskService.vectorSearch(QUERY, req.headers.token);
    res.json(response);
});

export default router;