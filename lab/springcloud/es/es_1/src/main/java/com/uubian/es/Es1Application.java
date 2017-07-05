package com.uubian.es;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.data.elasticsearch.repository.config.EnableElasticsearchRepositories;

@SpringBootApplication
@EnableElasticsearchRepositories
public class Es1Application {

	public static void main(String[] args) {
		SpringApplication.run(Es1Application.class, args);
	}
}
