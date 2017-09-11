package com.example.demo;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.EnableAutoConfiguration;
import org.springframework.boot.autoconfigure.SpringBootApplication;

import com.weibo.api.motan.common.MotanConstants;
import com.weibo.api.motan.config.springsupport.annotation.MotanReferer;
import com.weibo.api.motan.util.MotanSwitcherUtil;

@SpringBootApplication
@EnableAutoConfiguration
public class DemoClientApplication {

	
	
	public static void main(String[] args) {
		SpringApplication.run(DemoClientApplication.class, args);
		//MotanSwitcherUtil.setSwitcherValue(MotanConstants.REGISTRY_HEARTBEAT_SWITCHER, true);
	    //System.out.println("Client start ...");
	    
	}
	
}
