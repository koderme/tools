package com.gharat.rest.restpayload2.controller;

import java.util.concurrent.atomic.AtomicLong;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.http.HttpRequest;
import org.springframework.http.HttpStatus;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;

import com.gharat.rest.restpayload2.model.Employee;
import com.gharat.rest.restpayload2.model.Greeting;
@RestController
public class GreetingController {

	private static final Logger logger = LoggerFactory.getLogger(GreetingController.class);

    private static final String template = "Hello, %s!";
    private final AtomicLong counter = new AtomicLong();

    @RequestMapping("/greeting")
    public Greeting greeting(@RequestParam(value="name", defaultValue="World") String name) {
        return new Greeting(counter.incrementAndGet(),
                            String.format(template, name));
    }
  
    /*
    @RequestMapping(Request "/greeting-post")
    public Greeting greetingPost(String payload) {
        return new Greeting(counter.incrementAndGet(),
                            String.format(template, name));
    }
    */
    
    @PostMapping("/greeting-post")
	void greetingPost(String payload) {
		System.out.println("payload :" + payload);
	}
    
 // ---- save CustomerProfile
 	@RequestMapping(path = "save", method = RequestMethod.POST, 
 			produces = MediaType.APPLICATION_JSON_UTF8_VALUE, 
 			consumes = MediaType.APPLICATION_JSON_UTF8_VALUE)
 	public @ResponseBody ResponseEntity<Boolean> save(@RequestBody Employee emp) {

 		logger.info("save request {}", emp);
 		
 		if (emp == null)
 			return new ResponseEntity<>(false, HttpStatus.BAD_REQUEST);


 		boolean result = true;
 		
 		logger.info("result {}", result);
 		return result ? new ResponseEntity<>(result, HttpStatus.OK)
 				: new ResponseEntity<>(false, HttpStatus.BAD_REQUEST);
 	}
 	
 // ---- save CustomerProfile
  	@RequestMapping(path = "save2", method = RequestMethod.POST, 
  			produces = MediaType.APPLICATION_JSON_UTF8_VALUE, 
  			consumes = MediaType.APPLICATION_JSON_UTF8_VALUE)
  	public @ResponseBody ResponseEntity<Boolean> save2(Object inRequest) {

  		logger.info("save2 request {}", inRequest);
  		
  		if (inRequest == null )
  			return new ResponseEntity<>(false, HttpStatus.BAD_REQUEST);

  		logger.info("save2 request class {}", inRequest.getClass().getName());
  		

  		boolean result = true;
  		
  		logger.info("result {}", result);
  		return result ? new ResponseEntity<>(result, HttpStatus.OK)
  				: new ResponseEntity<>(false, HttpStatus.BAD_REQUEST);
  	}



}