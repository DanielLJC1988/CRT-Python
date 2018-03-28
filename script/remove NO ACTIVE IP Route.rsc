#������ʾno active��·���ַ�
#:local NoActive [/ip route find active !=yes];
#����ȡ���ַ����� RouterStr
#:local RouterStr [:pick $NoActive ];
#���δ����·����Ŀ����   [/len [/ip route find active !=yes]]
#�鿴�ű���ȷ��  system scheduler print detail where name=schedule1



#��һ�棬��̬����з�active·����Ŀ����
:for RemoveIP from=0 to=[/len [/ip route find active !=yes]] step=1 do={
 :if ([:resolve [/ip route find active !=yes] ] != "" ) do={ 
 /ip route remove numbers=[:pick [/ip route find active !=yes] ]
} else={
 :log info "RouterStr is null"
}
}



#�ڶ��棬�����ж��޷�����������(���������)����ִ��ɾ��·��,����ɾ��ȫ��·����Ŀ
#�ر�DNS���棬������󻺴�ʱ��Ϊ30��,���DNS����
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



#�����棬Ƕ��IF�ж��Ƿ���ڰ�������Ϊluosen�Ľӿڣ����ڲŻ�֧��ɾ��·��
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




#���İ棬�������
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

#��ʾ��ѯ��  ����ֱ��·�ɱ�
put [len [ip route find active =yes && connect && gateway =luosen  ]]

ip route print where static dynamic





#����ַ�����Ҳ����ӿ�����Ϊluosenʱ����luosen��L2TP�˿�disable
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

	
	
#Tools netwatch ���114.114.114.114ͨ�������ƿ��ؽӿں�·��
/interface enable luosen
/ip route enable numbers=1






#����ַ�����Ҳ����ӿ�����Ϊluosenʱ����luosen��L2TP�˿�disable�Ľ���V1.1
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

	
	

#�����жϽ���������+��ַ�����Ҳ����ӿ�����Ϊluosenʱ����luosen��L2TP�˿�disable�Ľ���V1.2
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
	
	
	
	
	
	
	
#����ַ�����Ҳ����ӿ�����Ϊluosenʱ����luosen��L2TP�˿�disable�Ľ���V1.3
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




#�������� ����ַ�����нӿ�Ϊpppoe�������Ҳ����ӿ�����Ϊscbchinawifiʱ����scbchinawifi��L2TP�˿�disable��enable
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
	
	
	
#��ѯ����·�ɱ�gateway��x.x.x.x��(ʵ�ʲ���ʱ�����x.x.x.x�滻��ԭ��·�ɱ����IP��ַ)�������޸�
:for SetGateway from=0 to=[/len [/ip route find gateway =x.x.x.x ]] step=1 do={
	/ip route set gateway= ��ȷ�����ص�ַ numbers=[:pick [/ip route find gateway =x.x.x.x ] ]
}