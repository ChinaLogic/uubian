package com.example.demo.service;

import org.springframework.stereotype.Service;

import com.weibo.api.motan.config.springsupport.annotation.MotanService;

@MotanService
public interface UserService {
	public String sayHello(String name);
}
