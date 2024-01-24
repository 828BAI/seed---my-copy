const express = require('express');

const fetch = (...args) => import('node-fetch').then(({default: fetch}) => fetch(...args));

const router = express.Router();

router.post('/api/project/create', async(req,res)=>{
    const{access} =req.cookies;
    const {project_name, desciption, investment, country, stage, industry, project_image, papers, video, presentation} =req.body;

    const body = JSON.stringify({
        project_name, desciption, investment, country, stage, industry, project_image, papers, video, presentation
    });
    try{
        const createProjectRes = await fetch(`${process.env.API_URL}/api/project/manage`, {
            method:'POST',
            headers:{
                Accept: 'application/json',
                'Content-Type': 'application/json',
                Authorization: `Bearer ${access}`
            },
            body,
        });
        const data = await registerRes.json();
        return res.status(createProjectRes.status).json();
    }

    catch (err){
        return res.status(500).json({
            error: "Something went wrong when creating a project"
        });
    }

});
module.exports = router;