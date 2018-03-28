#定义显示no active的路由字符
#:local NoActive [/ip route find active !=yes];
#定义取出字符变量 RouterStr
#:local RouterStr [:pick $NoActive ];
#查出未激活路由条目数量   [/len [/ip route find active !=yes]]
#查看脚本正确性  system scheduler print detail where name=schedule1



#第一版，动态查出有非active路由条目数量
:for RemoveIP from=0 to=[/len [/ip route find active !=yes]] step=1 do={
 :if ([:resolve [/ip route find active !=yes] ] != "" ) do={ 
 /ip route remove numbers=[:pick [/ip route find active !=yes] ]
} else={
 :log info "RouterStr is null"
}
}



#第二版，加入判断无法解析出域名(断网情况下)，不执行删除路由,避免删除全部路由条目
#关闭DNS缓存，设置最大缓存时间为30秒,清空DNS缓存
/ip dns set cache-max-ttl=30s
/ip dns set allow-remote-requests=no
/ip dns cache flush
:for RemoveIP from=0 to=[/len [/ip route find active !=yes]] step=1 do={
 :if ([:resolve access.fashion-tele.com ] != "failure: dns server failure" ) do={ 
 /ip route remove numbers=[:pick [/ip route find active !=yes] ]
} else={
:log info "RouterStr is null"
}
}



#第三版，嵌套IF判断是否存在包含名称为luosen的接口，存在才会支持删除路由
/ip dns set cache-max-ttl=0s
/ip dns set allow-remote-requests=yes
/ip dns cache flush
:for RemoveIP from=0 to=[/len [/ip route find active !=yes]] step=1 do={
 :if ([:resolve access.fashion-tele.com ] != "failure: dns server failure" ) do={ 
 
	:if ([:ip address find interface =luosen] != "" ) do={
	/ip route remove numbers=[:pick [/ip route find active !=yes] ]
	} else={
	/log info "remove route failure L2TP is down"
 }
} else={
/log info "remove route failure WAN is down"
}
}




#第四版，定义变量
:local RouteCount;
:local ResolveDomain;
:local FindL2tp;
:local RouteNumber;

:set RouteCount [/len [/ip route find active !=yes]];

/ip dns set cache-max-ttl=0s
/ip dns set allow-remote-requests=yes
/ip dns cache flush

:for RemoveIP from=0 to=$RouteCount step=1 do={
	:set ResolveDomain [:resolve access.fashion-tele.com ];
	:if ($ResolveDomain != "failure: dns server failure" ) do={ 
		:set FindL2tp [:ip address find interface =luosen];
		:if ($FindL2tp != "" ) do={
		:set RouteNumber [:pick [/ip route find active !=yes] ];
		/ip route remove numbers=$RouteNumber
		} else={
		/log info "remove route failure L2TP is down"
		}
	} else={
	/log info "remove route failure WAN is down"
	}
}

#显示查询出  存活的直连路由表
put [len [ip route find active =yes && connect && gateway =luosen  ]]

ip route print where static dynamic





#当地址表里找不到接口名称为luosen时，把luosen的L2TP端口disable
:local FindL2tp;


/ip dns set cache-max-ttl=0s
/ip dns set allow-remote-requests=yes
/ip dns cache flush


 
:set FindL2tp [:ip address find interface =luosen];
:if ($FindL2tp = "" ) do={
	/interface disable luosen
	} else={
	/log info "access.fashion-tele.com is alive, do not disable L2TP"
	}

	
	
#Tools netwatch 检测114.114.114.114通断来控制开关接口和路由
/interface enable luosen
/ip route enable numbers=1






#当地址表里找不到接口名称为luosen时，把luosen的L2TP端口disable改进版V1.1
:local FindL2tp; 
:local FindInterface; 
:set FindL2tp [:ip address find interface =luosen];
:set FindInterface [:interface find name =luosen];
:if ($FindInterface != "") do={
	:if ($FindL2tp = "" ) do={
		/interface disable luosen
		delay 60
		/interface enable luosen
		delay 20
		:if ( [:ip address find interface =luosen] = "" ) do={
			/system reboot
		} else={
			/log info "L2TP recover"
		}
		} else={
		}
	}

	
	

#加入判断解析域名，+地址表里找不到接口名称为luosen时，把luosen的L2TP端口disable改进版V1.2
:local FindL2tp;
:local FindInterface;
:local ResolveDomain;
:set FindL2tp [:ip address find interface =luosen];
:set FindInterface [:interface find name =luosen];
:set ResolveDomain [:resolve access.fashion-tele.com ];
/ip dns set cache-max-ttl=0s
/ip dns set allow-remote-requests=yes
/ip dns cache flush
:if ($ResolveDomain = "failure: dns server failure" ) do={
	:if ( [:interface l2tp-client find name =luosen connect-to =access.fashion-tele.com] !="" ) do={
		/log info "Domain error"
		/interface l2tp-client set numbers=luosen connect-to=222.73.198.139
		delay 5
		:if ($FindInterface != "") do={
			:if ($FindL2tp = "" ) do={
				/interface disable luosen
				delay 60
				/interface enable luosen
				delay 5
				:if ( [:ip address find interface =luosen] = "" ) do={
					/system reboot
				} else={
					/log info "L2TP recover"
				}
				} else={
				}
			}
		} else={
		:if ($FindInterface != "") do={
			:if ($FindL2tp = "" ) do={
				/interface disable luosen
				delay 60
				/interface enable luosen
				delay 5
				:if ( [:ip address find interface =luosen] = "" ) do={
					/system reboot
				} else={
					/log info "L2TP recover"
				}
				} else={
				}
			}
		}
		
	} else={
	:if ( [:interface l2tp-client find name =luosen connect-to =access.fashion-tele.com] ="" ) do={
		/log info "Domain recover"
		/interface l2tp-client set numbers=luosen connect-to=access.fashion-tele.com
		delay 5
		:if ($FindInterface != "") do={
			:if ($FindL2tp = "" ) do={
				/interface disable luosen
				delay 60
				/interface enable luosen
				delay 5
				:if ( [:ip address find interface =luosen] = "" ) do={
					/system reboot
				} else={
					/log info "L2TP recover"
				}
				} else={
				}
			}
		} else={
		:if ($FindInterface != "") do={
			:if ($FindL2tp = "" ) do={
				/interface disable luosen
				delay 60
				/interface enable luosen
				delay 5
				:if ( [:ip address find interface =luosen] = "" ) do={
					/system reboot
				} else={
					/log info "L2TP recover"
				}
				} else={
				}
			}
		}
	}
	
	
	
	
	
	
	
#当地址表里找不到接口名称为luosen时，把luosen的L2TP端口disable改进版V1.3
:local FindL2tp; 
:local FindInterface; 
:set FindL2tp [:ip address find interface =adidas];
:set FindInterface [:interface find name =adidas];
:if ($FindInterface != "") do={
	:if ($FindL2tp = "" ) do={
		/interface disable adidas
		delay 60
		/interface enable adidas
		delay 20
		:if ( [:ip address find interface =adidas] = "" ) do={
			:if ( [:interface l2tp-client find name =adidas connect-to =access.fashion-tele.com] !="" ) do={
				/interface l2tp-client set numbers=adidas connect-to=222.73.198.139
				delay 5
				:if ( [:ip address find interface =adidas] = "" ) do={
					/system reboot
				} else={
					/log info "change L2TP-address L2TP recover"
				}
			} else={
				/system reboot
			}
		} else={
			/log info "L2TP recover"
		}
	} else={
	}
} else={

}
:if ( [:resolve access.fashion-tele.com ] = "222.73.198.139" ) do={
	:if ( [:interface l2tp-client find name =adidas connect-to =access.fashion-tele.com] !="" ) do={
		
	} else={
		/interface l2tp-client set numbers=adidas connect-to=access.fashion-tele.com
		/log info "Domain recover access.fashion-tele.com"
	}
}




#渣打银行 当地址表里有接口为pppoe，并且找不到接口名称为scbchinawifi时，把scbchinawifi的L2TP端口disable再enable
:local FindL2tp;
:local FindPPPOE;
:local FindInterface;
:set FindL2tp [:ip address find interface =scbchinawifi];
:set FindPPPOE [:interface find name =pppoe];
:set FindInterface [:interface find name =scbchinawifi];
:if ($FindPPPOE != "") do={
	:if ($FindInterface != "") do={
		:if ($FindL2tp = "" ) do={
			/interface disable scbchinawifi
			delay 60
			/interface enable scbchinawifi
			delay 20
			:if ( [:ip address find interface =scbchinawifi] = "" ) do={
				/system reboot
			} else={
				/log info "L2TP recover"
			}
			} else={
			}
		}
	}
	
	
	
#查询所有路由表gateway是x.x.x.x的(实际操作时，请把x.x.x.x替换成原来路由表里的IP地址)，批量修改
:for SetGateway from=0 to=[/len [/ip route find gateway =x.x.x.x ]] step=1 do={
	/ip route set gateway= 正确的网关地址 numbers=[:pick [/ip route find gateway =x.x.x.x ] ]
}