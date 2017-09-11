package com.example.demo.controller;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.example.demo.service.GroupService;
import com.example.demo.service.UserService;
import com.weibo.api.motan.config.springsupport.annotation.MotanReferer;

@RestController
public class UserController {

	@MotanReferer(basicReferer = "basicRefererConfigBean")
	private UserService userService;
	
	@MotanReferer(basicReferer = "basicRefererConfigBean")
	private GroupService groupService;
	
	@RequestMapping("/say")
	public String say(){
		return userService.sayHello("world");
	}
	@RequestMapping("/cao")
	public String cao(){
		return groupService.cao("world");
	}
}
