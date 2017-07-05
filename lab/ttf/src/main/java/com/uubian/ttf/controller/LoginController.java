package com.uubian.ttf.controller;



import java.io.IOException;
import java.io.OutputStream;

import javax.servlet.http.HttpServletResponse;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;


@RestController()
@RequestMapping("/ttf")
public class LoginController {

	@GetMapping("/ttf/{text}/{filename}")
	public void getAll(@PathVariable String text,HttpServletResponse respone) throws IOException, Exception{
		
		OutputStream out=respone.getOutputStream();
		
		TTS ttsDemo = new TTS();
		ttsDemo.setTts_text(text);
		ttsDemo.setOut(out);
    	ttsDemo.startTTS();
    	ttsDemo.shutDown();
		
		
	}
	
}
