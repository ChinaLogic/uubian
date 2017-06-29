package com.uubian.login.controller;


import java.net.URI;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.cloud.client.ServiceInstance;
import org.springframework.cloud.client.discovery.DiscoveryClient;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.client.RestTemplate;
import com.uubian.login.domain.UserBase;

@RestController()
@RequestMapping("/login")
public class LoginController {
	@Autowired
    DiscoveryClient client;
	@Autowired
	private RestTemplate restTemplate;
	
	@GetMapping("/login")
	public List<UserBase>   getAll(){
		
		//return restTemplate.getForObject("http://localhost:2001/userbase/getAllList", List.class);
		List<ServiceInstance> list = client.getInstances("USERBASE");
        if (list != null && list.size() > 0 ) {
            URI uri = list.get(0).getUri();
            if (uri !=null ) {
                return restTemplate.getForObject(uri+"/userbase/getAllList",List.class);
            }
        }
		return null;
	}
	
}
