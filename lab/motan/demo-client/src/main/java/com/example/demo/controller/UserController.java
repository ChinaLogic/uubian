package com.example.demo.controller;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.example.demo.service.UserService;
import com.weibo.api.motan.config.springsupport.annotation.MotanReferer;

@RestController
public class UserController {

	@MotanReferer
	private UserService userService;
	
	
	@RequestMapping("/say")
	public String say(){
		return userService.sayHello("world");
	}
	
}
