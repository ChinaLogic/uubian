package com.example.demo;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import com.weibo.api.motan.config.springsupport.AnnotationBean;
import com.weibo.api.motan.config.springsupport.BasicServiceConfigBean;
import com.weibo.api.motan.config.springsupport.ProtocolConfigBean;
import com.weibo.api.motan.config.springsupport.RegistryConfigBean;

@Configuration
	public class MotanConfiguration {



	  
	  
	  @Bean
	    public AnnotationBean motanAnnotationBean() {
	        AnnotationBean motanAnnotationBean = new AnnotationBean();
	        //motanAnnotationBean.setPackage("com.example.demo.controller");
	        return motanAnnotationBean;
	    }

	    @Bean(name = "motan")
	    public ProtocolConfigBean protocolConfig() {
	        ProtocolConfigBean config = new ProtocolConfigBean();
	        config.setDefault(true);
	        config.setName("motan");
	        config.setMaxContentLength(1048576);
	        return config;
	    }

	    @Bean(name = "registryConfig")
	    public RegistryConfigBean registryConfig() {
	        RegistryConfigBean config = new RegistryConfigBean();
	        config.setRegProtocol("zookeeper");
		    config.setAddress("127.0.0.1:2181");
	        return config;
	    }

	    @Bean
	    public BasicServiceConfigBean baseServiceConfig() {
	        BasicServiceConfigBean config = new BasicServiceConfigBean();
	        config.setExport("motan:8002");
	        config.setGroup("testgroup");
	        config.setAccessLog(false);
	        config.setShareChannel(true);
	        config.setApplication("UserService1");
	        config.setRegistry("registryConfig");
	        return config;
	    }
	  
}
