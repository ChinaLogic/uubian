package com.example.demo.service;


import com.weibo.api.motan.config.springsupport.annotation.MotanService;

@MotanService
public class GroupServiceImpl implements GroupService{

	
	public String cao(String name) {
		System.out.println("3------------------------------->");
		return "caonima"+name;
	}

}
