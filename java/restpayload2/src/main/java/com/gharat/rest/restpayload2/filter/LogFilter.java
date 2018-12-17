package com.gharat.rest.restpayload2.filter;

import java.io.IOException;

import javax.servlet.Filter;
import javax.servlet.FilterChain;
import javax.servlet.FilterConfig;
import javax.servlet.ServletException;
import javax.servlet.ServletRequest;
import javax.servlet.ServletResponse;

import org.apache.catalina.connector.RequestFacade;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.context.annotation.Configuration;
import org.springframework.core.Ordered;
import org.springframework.core.annotation.Order;

@Configuration
@Order(Ordered.HIGHEST_PRECEDENCE)
public class LogFilter implements Filter {

 private static final Logger LOGGER = LoggerFactory.getLogger(LogFilter.class);

 @Override
 public void init(FilterConfig filterConfig) throws ServletException {
  LOGGER.info("########## Initiating Log filter ##########");
 }

 @Override
 public void doFilter(ServletRequest servletRequest, ServletResponse servletResponse, FilterChain filterChain) throws IOException, ServletException {

  //HttpServletRequest request = (HttpServletRequest) servletRequest;
  //HttpServletResponse response = (HttpServletResponse) servletRequest;
	 
	 org.apache.catalina.connector.RequestFacade rf = (RequestFacade)servletRequest;
	 
	 LOGGER.info("logfilter : {} ", rf.toString());

	 javax.servlet.ServletInputStream	 inStream = rf.getInputStream();
	 byte[] b = new byte[200];
	 inStream.readLine(b, 0, 100);
	 LOGGER.info("logfilter: bytes {}", new String(b));
	 
  //call next filter in the filter chain
  filterChain.doFilter(servletRequest, servletResponse);

  LOGGER.info("Logging Response :{}", servletResponse);
 }

 @Override
 public void destroy() {
  // TODO: 7/4/18
 }
}