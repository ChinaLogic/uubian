package com.example.demo.service;


import com.weibo.api.motan.config.springsupport.annotation.MotanService;

@MotanService
public class UserServiceImpl implements UserService{

	
	public String sayHello(String name) {
		System.out.println("1------------------------------->");
		return "hello1"+name;
	}

}
